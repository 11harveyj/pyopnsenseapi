"""OPNsense diagnostics.dns_diagnostics module."""

from pyopnsenseapi.modules.diagnostics.const import (ENDPOINTS)

DNS_DIAGNOSTICS_GET = "dns_diagnostics.get"
DNS_DIAGNOSTICS_SET = "dns_diagnostics.set"

class DnsDiagnostics(object):
    """OPNsense diagnostics.dns_diagnostics module."""

    @staticmethod
    def get(client):
        """Unsure what this is currently."""
        return client.get(ENDPOINTS.get(DNS_DIAGNOSTICS_GET))

    @staticmethod
    def set(client):
        """Unsure what this is currently."""
        return client.get(ENDPOINTS.get(DNS_DIAGNOSTICS_SET))
