"""The Pluxee integration."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv
from pluxee import PluxeeAsyncClient

from .const import CONF_PASSWORD, CONF_USERNAME, DOMAIN
from .coordinator import PluxeeCoordinator

CONFIG_SCHEMA = cv.config_entry_only_config_schema(DOMAIN)

PLATFORMS = ["sensor"]

type PluxeeConfigEntry = ConfigEntry[PluxeeCoordinator]


async def async_setup_entry(hass: HomeAssistant, entry: PluxeeConfigEntry) -> bool:
    """Set up Pluxee from a config entry."""
    api = PluxeeAsyncClient(entry.data[CONF_USERNAME], entry.data[CONF_PASSWORD])
    coordinator = PluxeeCoordinator(hass, api)

    await coordinator.async_config_entry_first_refresh()

    entry.runtime_data = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: PluxeeConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
