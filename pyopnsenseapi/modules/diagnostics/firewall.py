"""OPNsense diagnostics.firewall module."""

from pyopnsenseapi.modules.diagnostics.const import (ENDPOINTS)

FIREWALL_DEL_STATE = "firewall.delState"
FIREWALL_FLUSH_SOURCES = "firewall.flushSources"
FIREWALL_FLUSH_STATES = "firewall.flushStates"
FIREWALL_KILL_STATES = "firewall.killStates"
FIREWALL_LIST_RULE_IDS = "firewall.listRuleIds"
FIREWALL_LOG = "firewall.log"
FIREWALL_LOG_FILTERS = "firewall.logFilters"
FIREWALL_PF_STATS = "firewall.pfStatistics?$section=%s"
FIREWALL_Q_PF_TOP = "firewall.queryPfTop"
FIREWALL_Q_STATES = "firewall.queryStates"
FIREWALL_STATS = "firewall.stats"

class Firewall(object):
    """OPNsense diagnostics.firewall module."""

    @staticmethod
    def delete_state(client, stateid: str, creatorid: str):
        """Deletes a given state."""
        return client.post(
            endpoint=ENDPOINTS.get(FIREWALL_DEL_STATE),
            body={"stateid": stateid, "creatorid": creatorid}
        )

    @staticmethod
    def flush_sources(client):
        """Flushes sources."""
        return client.post(
            endpoint=ENDPOINTS.get(FIREWALL_FLUSH_SOURCES),
            body={}
        )

    @staticmethod
    def flush_states(client):
        """Flushes states."""
        return client.post(
            endpoint=ENDPOINTS.get(FIREWALL_FLUSH_STATES),
            body={}
        )

    @staticmethod
    def kill_states(client):
        """Kills states."""
        return client.post(
            endpoint=ENDPOINTS.get(FIREWALL_KILL_STATES),
            body={}
        )

    @staticmethod
    def get_rule_ids(client):
        """Gets a list of rule IDs."""
        return client.get(ENDPOINTS.get(FIREWALL_LIST_RULE_IDS))

    @staticmethod
    def get_firewall_log(client):
        """Returns the firewall log."""
        return client.get(ENDPOINTS.get(FIREWALL_LOG))

    @staticmethod
    def get_firewall_log_filters(client):
        """Returns firewall log filters?."""
        return client.get(ENDPOINTS.get(FIREWALL_LOG_FILTERS))

    @staticmethod
    def get_pf_statistics(client, section: str="null"):
        """Returns pfStatistics."""
        return client.get(str(ENDPOINTS.get(FIREWALL_PF_STATS)).format(section))

    @staticmethod
    def search_pf_top(client,
                      row_count: int = 500,
                      current_page: int = 1,
                      rule_id: str = "",
                      sort: str = "",
                      search_phrase: str = ""):
        """Returns pfTop."""
        return client.post(
            endpoint=ENDPOINTS.get(FIREWALL_Q_PF_TOP),
            body={
                "searchPhrase": search_phrase,
                "rowCount": row_count,
                "current": current_page,
                "ruleid": rule_id,
                "sort": sort
            })

    @staticmethod
    def search_states(client,
                      row_count: int = 500,
                      current_page: int = 1,
                      rule_id: str = "",
                      sort: str = "",
                      search_phrase: str = ""):
        """Returns pfTop."""
        return client.post(
            endpoint=ENDPOINTS.get(FIREWALL_Q_STATES),
            body={
                "searchPhrase": search_phrase,
                "rowCount": row_count,
                "current": current_page,
                "ruleid": rule_id,
                "sort": sort
            })

    @staticmethod
    def get_statistics(client):
        """Returns statistics."""
        return client.get(ENDPOINTS.get(FIREWALL_STATS))
