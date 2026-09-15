"""Generic BLE peripheral emulator for macOS (CoreBluetooth peripheral mode).

Advertises a local name and GATT service/characteristics as described by a
DeviceProfile, and routes incoming writes through the profile's command
handler. See devices/ for per-device profiles and README.md for usage.
"""

from dataclasses import dataclass
from typing import Callable, Optional

import objc
from CoreBluetooth import (
    CBAttributePermissionsReadable,
    CBAttributePermissionsWriteable,
    CBCharacteristicPropertyNotify,
    CBCharacteristicPropertyWrite,
    CBCharacteristicPropertyWriteWithoutResponse,
    CBMutableCharacteristic,
    CBMutableService,
    CBPeripheralManager,
    CBPeripheralManagerStatePoweredOn,
    CBUUID,
)
from Foundation import NSData, NSObject
from PyObjCTools import AppHelper

try:
    from CoreBluetooth import CBAdvertisementDataLocalNameKey as LOCAL_NAME_KEY
except ImportError:
    LOCAL_NAME_KEY = "kCBAdvDataLocalName"


@dataclass(frozen=True)
class DeviceProfile:
    """Static description of a BLE peripheral to emulate."""

    name: str  # advertised local name
    service_uuid: str
    tx_uuid: str  # central -> peripheral, write / write-without-response
    on_command: Callable[[str], Optional[str]]  # reply string, or None for no reply
    rx_uuid: Optional[str] = None  # peripheral -> central, notify (omit if device has none)


class _PeripheralDelegate(NSObject):
    def initWithProfile_(self, profile: DeviceProfile):
        self = objc.super(_PeripheralDelegate, self).init()
        if self is None:
            return None
        self.profile = profile
        self.rx_char = None
        return self

    def peripheralManagerDidUpdateState_(self, peripheral):
        print(f"[state] {peripheral.state()}")
        if peripheral.state() != CBPeripheralManagerStatePoweredOn:
            return

        chars = [
            CBMutableCharacteristic.alloc().initWithType_properties_value_permissions_(
                CBUUID.UUIDWithString_(self.profile.tx_uuid),
                CBCharacteristicPropertyWrite | CBCharacteristicPropertyWriteWithoutResponse,
                None,
                CBAttributePermissionsWriteable,
            )
        ]

        if self.profile.rx_uuid:
            self.rx_char = CBMutableCharacteristic.alloc().initWithType_properties_value_permissions_(
                CBUUID.UUIDWithString_(self.profile.rx_uuid),
                CBCharacteristicPropertyNotify,
                None,
                CBAttributePermissionsReadable,
            )
            chars.append(self.rx_char)

        service = CBMutableService.alloc().initWithType_primary_(
            CBUUID.UUIDWithString_(self.profile.service_uuid), True
        )
        service.setCharacteristics_(chars)
        peripheral.addService_(service)

    def peripheralManager_didAddService_error_(self, peripheral, service, error):
        if error is not None:
            print(f"[error] failed to add service: {error}")
            return
        peripheral.startAdvertising_({LOCAL_NAME_KEY: self.profile.name})

    def peripheralManagerDidStartAdvertising_error_(self, peripheral, error):
        if error is not None:
            print(f"[error] failed to start advertising: {error}")
        else:
            print(f"[advertising] broadcasting as {self.profile.name!r}")

    def peripheralManager_central_didSubscribeToCharacteristic_(self, peripheral, central, characteristic):
        print(f"[subscribe] {characteristic.UUID()}")

    def peripheralManager_didReceiveWriteRequests_(self, peripheral, requests):
        for request in requests:
            data = request.value()
            text = bytes(data).decode("utf-8", errors="replace") if data else ""
            print(f"[RX] {text!r}")
            self._reply_to(peripheral, text)
        # NimBLE's write-with-response path expects an ATT response to proceed.
        peripheral.respondToRequest_withResult_(requests[0], 0)

    def _reply_to(self, peripheral, text):
        if not self.rx_char:
            return
        for command in text.split(";"):
            command = command.strip()
            if not command:
                continue
            reply = self.profile.on_command(command)
            if reply is None:
                continue
            print(f"[TX] {reply!r}")
            payload = NSData.dataWithBytes_length_(reply.encode("utf-8"), len(reply))
            peripheral.updateValue_forCharacteristic_onSubscribedCentrals_(payload, self.rx_char, None)


def run(profile: DeviceProfile) -> None:
    """Advertise `profile` and print incoming writes until interrupted."""
    delegate = _PeripheralDelegate.alloc().initWithProfile_(profile)
    manager = CBPeripheralManager.alloc().initWithDelegate_queue_(delegate, None)
    print(f"Starting {profile.name} emulator (Ctrl+C to stop)...")
    # `manager` must stay referenced for the whole call below: CoreBluetooth
    # frees an unreferenced CBPeripheralManager before it can call back.
    AppHelper.runConsoleEventLoop(installInterrupt=True)
