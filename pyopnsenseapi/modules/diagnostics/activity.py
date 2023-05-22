"""OPNsense diagnostics.activity module."""

from pyopnsenseapi.modules.diagnostics.const import (ENDPOINTS)

ACTIVITY_GET_ACTIVITY = "activity.getActivity"

class Activity(object):
    """OPNsense diagnostics.activity module."""

    @staticmethod
    def get(client):
        """Return current system activity."""
        return client.get(ENDPOINTS.get(ACTIVITY_GET_ACTIVITY))
