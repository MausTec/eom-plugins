"""Lovense Max: vibration motor + pneumatic air actuator. Model type 'B'."""

from emulator import DeviceProfile

from .lovense_common import RX_UUID, SERVICE_UUID, TX_UUID, common_reply

MODEL_TYPE = "B"

PROFILE = DeviceProfile(
    name="LVS-Max-EMU",
    service_uuid=SERVICE_UUID,
    tx_uuid=TX_UUID,
    rx_uuid=RX_UUID,
    on_command=lambda command: common_reply(MODEL_TYPE, command) or "OK;",
)
