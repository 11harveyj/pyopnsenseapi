"""OPNsense DNS diagnostics."""

from pyopnsenseapi.modules.diagnostics.const import (ENDPOINTS)

DNS_REVERSE_LOOKUP = "dns.reverseLookup"

class Dns(object):
    """OPNsense diagnostics.dns module."""

    @staticmethod
    def reverse_lookup(client, address: str):
        """Return current system activity."""
        return client.get(ENDPOINTS.get(DNS_REVERSE_LOOKUP).format(address), True)
