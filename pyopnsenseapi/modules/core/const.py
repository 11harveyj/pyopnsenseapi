"""firmware module const"""

CORE = "core"

FUNCTIONS = {
    "FIRMWARE_POWER_OFF": "firmware.poweroff",
    "FIRMWARE_REBOOT": "firmware.reboot",
    "FIRMWARE_RUNNING": "firmware.running",
    "FIRMWARE_GET_FIRMWARE_CONFIG": "firmware.getFirmwareConfig",
    "FIRMWARE_GET_FIRMWARE_OPTIONS": "firmware.getFirmwareOptions",
    "FIRMWARE_SET_FIRMWARE_CONFIG": "firmware.setFirmwareConfig",
    "FIRMWARE_INFO": "firmware.info",
    "FIRMWARE_STATUS": "firmware.status",
    "FIRMWARE_AUDIT": "firmware.audit",
    "FIRMWARE_UPDATE": "firmware.update",
    "FIRMWARE_UPGRADE": "firmware.upgrade",
    "FIRMWARE_UPGRADE_STATUS": "firmware.upgradestatus",
    "FIRMWARE_CHANGELOG": "firmware.changelog?$version=%s",
    "FIRMWARE_INSTALL": "firmware.install",
    "FIRMWARE_REINSTALL": "firmware.reinstall",
    "FIRMWARE_REMOVE": "firmware.remove",
    "FIRMWARE_LOCK": "firmware.lock",
    "FIRMWARE_UNLOCK": "firmware.unlock",
    "FIRMWARE_DETAILS": "firmware.details",
    "FIRMWARE_LICENSE": "firmware.license"
}

# Dynamic build endpoints
ENDPOINTS = {}
for v in FUNCTIONS.items():
    ENDPOINTS[str(v[1])] = f"{CORE}/{str(v[1]).replace('.', '/')}"
