"""OPNsense diagnostics.interface module."""

from enum import Enum
from pyopnsenseapi.modules.diagnostics.const import (ENDPOINTS)

INTERFACE_CARP_STATUS = "interface.CarpStatus?$status=%s"
INTERFACE_DEL_ROUTE = "interface.delRoute"
INTERFACE_FLUSH_ARP = "interface.flushArp"
INTERFACE_GET_ARP = "interface.getArp"
INTERFACE_GET_BPF_STATS = "interface.getBpfStatistics"
INTERFACE_GET_CONFIG = "interface.getInterfaceConfig"
INTERFACE_GET_NAMES = "interface.getInterfaceNames"
INTERFACE_GET_STATS = "interface.getInterfaceStatistics"
INTERFACE_GET_MEM_STATS = "interface.getMemoryStatistics"
INTERFACE_GET_NDP = "interface.getNdp"
INTERFACE_GET_NETISR_STATS = "interface.getNetisrStatistics"
INTERFACE_GET_PFSYNC_NODES = "interface.getPfSyncNodes"
INTERFACE_GET_PROTO_STATS = "interface.getProtocolStatistics"
INTERFACE_GET_ROUTES = "interface.getRoutes"
INTERFACE_GET_SOCKET_STATS = "interface.getSocketStatistics"
INTERFACE_GET_VIP_STATUS = "interface.getVipStatus"
INTERFACE_SEARCH_ARP = "interface.searchArp"
INTERFACE_SEARCH_NDP = "interface.searchNdp"

class CarpStatus(Enum):
    """Valid CARP status values"""
    ENABLE = "enable"
    DISABLE = "disable"
    MAINTENANCE = "maintenance"

    def __str__(self) -> str:
        return self.value

class Interface(object):
    """OPNsense diagnostics.interface module."""

    @staticmethod
    def set_carp_status(client, status: CarpStatus):
        """Set new carp node status."""
        return client.post(
            endpoint=str(ENDPOINTS.get(INTERFACE_CARP_STATUS)).format(str(status))
        )

    @staticmethod
    def del_route(client, destination: str, gateway: str):
        """Deletes a route."""
        return client.post(
            endpoint=ENDPOINTS.get(INTERFACE_DEL_ROUTE),
            body={
                "destination": destination,
                "gateway": gateway
            }
        )

    @staticmethod
    def flush_arp(client):
        """Flush system arp cache."""
        return client.post(
            endpoint=ENDPOINTS.get(INTERFACE_FLUSH_ARP),
            body={}
        )

    @staticmethod
    def get_arp(client):
        """Get ARP table."""
        return client.get(
            endpoint=ENDPOINTS.get(INTERFACE_GET_ARP)
        )

    @staticmethod
    def get_bpf_statistics(client):
        """Get BPF statistics."""
        return client.get(
            endpoint=ENDPOINTS.get(INTERFACE_GET_BPF_STATS)
        )

    @staticmethod
    def get_config(client):
        """Get interface config."""
        return client.get(
            endpoint=ENDPOINTS.get(INTERFACE_GET_CONFIG)
        )

    @staticmethod
    def get_interface_names(client):
        """Get interface name(s)."""
        return client.get(
            endpoint=ENDPOINTS.get(INTERFACE_GET_NAMES)
        )

    @staticmethod
    def get_statistics(client):
        """Get interface stats."""
        return client.get(
            endpoint=ENDPOINTS.get(INTERFACE_GET_STATS)
        )

    @staticmethod
    def get_memory_statistics(client):
        """Get interface memory stats."""
        return client.get(
            endpoint=ENDPOINTS.get(INTERFACE_GET_MEM_STATS)
        )

    @staticmethod
    def get_ndp(client):
        """Get NDP table."""
        return client.get(
            endpoint=ENDPOINTS.get(INTERFACE_GET_NDP)
        )

    @staticmethod
    def get_netisr_statistics(client):
        """Get netisr statistics."""
        return client.get(
            endpoint=ENDPOINTS.get(INTERFACE_GET_NETISR_STATS)
        )

    @staticmethod
    def get_pfsync_nodes(client):
        """Get PFSync nodes."""
        return client.get(
            endpoint=ENDPOINTS.get(INTERFACE_GET_PFSYNC_NODES)
        )

    @staticmethod
    def get_protocol_statistics(client):
        """Get interface protocol stats."""
        return client.get(
            endpoint=ENDPOINTS.get(INTERFACE_GET_PROTO_STATS)
        )

    @staticmethod
    def get_routes(client):
        """Get routes."""
        return client.get(
            endpoint=ENDPOINTS.get(INTERFACE_GET_ROUTES)
        )

    @staticmethod
    def get_socket_statistics(client):
        """Get interface socket stats."""
        return client.get(
            endpoint=ENDPOINTS.get(INTERFACE_GET_SOCKET_STATS)
        )

    @staticmethod
    def get_vip_status(client):
        """Get VIP status."""
        return client.get(
            endpoint=ENDPOINTS.get(INTERFACE_GET_VIP_STATUS)
        )

    @staticmethod
    def search_arp_table(client,
                      row_count: int = 500,
                      current_page: int = 1,
                      rule_id: str = "",
                      sort: str = "",
                      search_phrase: str = ""):
        """Returns pfTop."""
        return client.post(
            endpoint=ENDPOINTS.get(INTERFACE_SEARCH_ARP),
            body={
                "searchPhrase": search_phrase,
                "rowCount": row_count,
                "current": current_page,
                "ruleid": rule_id,
                "sort": sort
            })

    @staticmethod
    def search_ndp_table(client,
                      row_count: int = 500,
                      current_page: int = 1,
                      rule_id: str = "",
                      sort: str = "",
                      search_phrase: str = ""):
        """Returns pfTop."""
        return client.post(
            endpoint=ENDPOINTS.get(INTERFACE_SEARCH_NDP),
            body={
                "searchPhrase": search_phrase,
                "rowCount": row_count,
                "current": current_page,
                "ruleid": rule_id,
                "sort": sort
            })
