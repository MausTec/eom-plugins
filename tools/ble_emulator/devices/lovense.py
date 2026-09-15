"""Generic single-motor Lovense vibrator (Lush, Hush, Ambi, Domi, ...).

Model type is arbitrary here since the generic driver never inspects DeviceType,
it only sends Vibrate:N;. 'S' (Lush) is used as a representative default.
"""

from emulator import DeviceProfile

from .lovense_common import RX_UUID, SERVICE_UUID, TX_UUID, common_reply

MODEL_TYPE = "S"

PROFILE = DeviceProfile(
    name="LVS-EMU",
    service_uuid=SERVICE_UUID,
    tx_uuid=TX_UUID,
    rx_uuid=RX_UUID,
    on_command=lambda command: common_reply(MODEL_TYPE, command) or "OK;",
)
