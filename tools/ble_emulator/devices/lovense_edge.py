"""Lovense Edge / Edge 2: dual independent vibration motors. Model type 'P'."""

from emulator import DeviceProfile

from .lovense_common import RX_UUID, SERVICE_UUID, TX_UUID, common_reply

MODEL_TYPE = "P"

PROFILE = DeviceProfile(
    name="LVS-Edge-EMU",
    service_uuid=SERVICE_UUID,
    tx_uuid=TX_UUID,
    rx_uuid=RX_UUID,
    on_command=lambda command: common_reply(MODEL_TYPE, command) or "OK;",
)
