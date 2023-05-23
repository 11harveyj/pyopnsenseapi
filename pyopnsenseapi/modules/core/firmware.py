"""OPNsense core.firmware module."""

from pyopnsenseapi.modules.core.const import (ENDPOINTS)
from pyopnsenseapi.modules.enums import PackageManagerActions

FIRMWARE_POWER_OFF = "firmware.poweroff"
FIRMWARE_REBOOT = "firmware.reboot"
FIRMWARE_RUNNING = "firmware.running"
FIRMWARE_GET_FIRMWARE_CONFIG = "firmware.getFirmwareConfig"
FIRMWARE_GET_FIRMWARE_OPTIONS = "firmware.getFirmwareOptions"
FIRMWARE_SET_FIRMWARE_CONFIG = "firmware.setFirmwareConfig"
FIRMWARE_INFO = "firmware.info"
FIRMWARE_STATUS = "firmware.status"
FIRMWARE_AUDIT = "firmware.audit"
FIRMWARE_UPDATE = "firmware.update"
FIRMWARE_UPGRADE = "firmware.upgrade"
FIRMWARE_UPGRADE_STATUS = "firmware.upgradestatus"
FIRMWARE_CHANGELOG = "firmware.changelog?$version=%s"
FIRMWARE_INSTALL = "firmware.install"
FIRMWARE_REINSTALL = "firmware.reinstall"
FIRMWARE_REMOVE = "firmware.remove"
FIRMWARE_LOCK = "firmware.lock"
FIRMWARE_UNLOCK = "firmware.unlock"
FIRMWARE_DETAILS = "firmware.details"
FIRMWARE_LICENSE = "firmware.license"


class Firmware(object):
    """OPNsense core.firmware module."""

    is_controller = True

    def __init__(self, client) -> None:
        self._client = client

    def power_off(self):
        """Powers the OPNsense system down."""
        return self._client.post(
            endpoint=ENDPOINTS.get(FIRMWARE_POWER_OFF),
            body={}
        )

    def reboot(self):
        """Reboot the OPNsense system."""
        return self._client.post(
            endpoint=ENDPOINTS.get(FIRMWARE_REBOOT),
            body={}
        )

    def running(self):
        """Gets execution status."""
        return self._client.get(
            endpoint=ENDPOINTS.get(FIRMWARE_RUNNING)
        )

    def get_firmware_config(self):
        """Gets the firmware config."""
        return self._client.get(
            endpoint=ENDPOINTS.get(FIRMWARE_GET_FIRMWARE_CONFIG)
        )

    def get_firmware_options(self):
        """Gets the firmware options."""
        return self._client.get(
            endpoint=ENDPOINTS.get(FIRMWARE_GET_FIRMWARE_OPTIONS)
        )

    def set_firmware_config(self, fw_config: dict):
        """Set the firmware config."""
        return self._client.post(
            endpoint=ENDPOINTS.get(FIRMWARE_SET_FIRMWARE_CONFIG),
            body=fw_config
        )

    def info(self):
        """Gets the system info."""
        return self._client.get(
            endpoint=ENDPOINTS.get(FIRMWARE_INFO)
        )

    def status(self, run_probe: bool = False):
        """Gets the firmware status."""
        if run_probe:
            return self._client.post(
                endpoint=ENDPOINTS.get(FIRMWARE_STATUS),
                body={}
            )
        else:
            return self._client.get(
                endpoint=ENDPOINTS.get(FIRMWARE_STATUS)
            )

    def run_audit(self):
        """Runs a firmware audit."""
        return self._client.post(
            endpoint=ENDPOINTS.get(FIRMWARE_AUDIT),
            body={}
        )

    def run_update(self):
        """Runs a firmware update."""
        return self._client.post(
            endpoint=ENDPOINTS.get(FIRMWARE_UPDATE),
            body={}
        )

    def run_upgrade(self):
        """Runs a firmware upgrade."""
        return self._client.post(
            endpoint=ENDPOINTS.get(FIRMWARE_UPGRADE),
            body={}
        )

    def upgrade_status(self):
        """Gets firmware upgrade status."""
        return self._client.get(
            endpoint=ENDPOINTS.get(FIRMWARE_UPGRADE_STATUS)
        )

    def changelog(self,
                    version: str):
        """Gets the changelog for a given version."""
        return self._client.post(
            endpoint=str(ENDPOINTS.get(FIRMWARE_CHANGELOG)).format(version),
            body={}
        )

    def pack_man(self,
                 pkg_name: str,
                 action: PackageManagerActions = PackageManagerActions.DETAILS):
        """OPNsense package manager."""
        return True
