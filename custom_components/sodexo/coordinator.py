"""DataUpdateCoordinator for Pluxee."""

from __future__ import annotations

import logging
from datetime import timedelta

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from pluxee import PluxeeAsyncClient, PluxeeBalance, PluxeeLoginError

_LOGGER = logging.getLogger(__name__)

UPDATE_INTERVAL = timedelta(minutes=60)


class PluxeeCoordinator(DataUpdateCoordinator[PluxeeBalance]):
    """Coordinator to fetch Pluxee balance data."""

    def __init__(self, hass: HomeAssistant, api: PluxeeAsyncClient) -> None:
        """Initialize the coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name="Pluxee",
            update_interval=UPDATE_INTERVAL,
        )
        self.api = api

    async def _async_update_data(self) -> PluxeeBalance:
        """Fetch balance from the Pluxee API."""
        try:
            return await self.api.get_balance()
        except PluxeeLoginError as err:
            raise UpdateFailed(f"Authentication failed: {err}") from err
        except Exception as err:
            raise UpdateFailed(f"Error fetching Pluxee data: {err}") from err
