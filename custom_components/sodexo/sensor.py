"""Platform for sensor integration."""
from __future__ import annotations
from typing import Any
import logging

from datetime import timedelta
from typing import Any, Callable, Dict

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from pluxee import PluxeeAsyncClient
from .const import (
    COUNTRY_BE, DOMAIN, DEFAULT_ICON, UNIT_OF_MEASUREMENT,
    CONF_COUNTRY, CONF_USERNAME, CONF_PASSWORD,
    ATTRIBUTION
)

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)

# Time between updating data from API
SCAN_INTERVAL = timedelta(minutes=60)


async def async_setup_entry(hass: HomeAssistant,
                            config_entry: ConfigEntry,
                            async_add_entities: Callable):
    """Setup sensor platform."""
    config = config_entry.data
    api = PluxeeAsyncClient(config[CONF_USERNAME], config[CONF_PASSWORD])

    sensors = [
        SodexoLunchPassSensor(api, config),
        SodexoEcoPassSensor(api, config),
        SodexoGiftPassSensor(api, config)
    ]
    async_add_entities(sensors, update_before_add=True)


class SodexoSensor(SensorEntity):
    """Representation of a Sodexo Card (Sensor)."""

    def __init__(self, api: PluxeeAsyncClient, config: Any):
        super().__init__()
        self._api = api
        self._config = config
        self._updated = None

        self._icon = DEFAULT_ICON
        self._unit_of_measurement = UNIT_OF_MEASUREMENT
        self._device_class = SensorDeviceClass.MONETARY
        self._state_class = SensorStateClass.TOTAL
        self._state = None
        self._available = False

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        return self._available

    @property
    def state(self) -> float:
        return self._state

    @property
    def device_class(self):
        return self._device_class

    @property
    def state_class(self):
        return self._state_class

    @property
    def unit_of_measurement(self):
        """Return the unit the value is expressed in."""
        return self._unit_of_measurement

    @property
    def icon(self):
        return self._icon

    @property
    def attribution(self):
        return ATTRIBUTION

    @property
    def extra_state_attributes(self) -> Dict[str, Any]:
        """Return the state attributes."""
        return {
            "updated": self._updated
        }


class SodexoLunchPassSensor(SodexoSensor):
    @property
    def name(self) -> str:
        """Return the name of the entity."""
        return "Sodexo Lunch amount"

    @property
    def unique_id(self) -> str:
        """Return the unique ID of the sensor."""
        return f"{DOMAIN}-{self._config[CONF_USERNAME]}-LUNCH".lower()

    async def async_update(self) -> None:
        api = self._api

        try:
            account = await api.get_balance()
            self._state = account.lunch_pass
            self._updated = True
            self._available = True

        except Exception as err:
            self._available = False
            _LOGGER.exception("Error updating data from DGEG API.", err)


class SodexoGiftPassSensor(SodexoSensor):
    @property
    def name(self) -> str:
        """Return the name of the entity."""
        return "Sodexo Gift amount"

    @property
    def unique_id(self) -> str:
        """Return the unique ID of the sensor."""
        return f"{DOMAIN}-{self._config[CONF_USERNAME]}-GIFT".lower()

    async def async_update(self) -> None:
        api = self._api

        try:
            account = await api.get_balance()
            self._state = account.gift_pass
            self._updated = True
            self._available = True

        except Exception as err:
            self._available = False
            _LOGGER.exception("Error updating data from DGEG API.", err)


class SodexoEcoPassSensor(SodexoSensor):
    @property
    def name(self) -> str:
        """Return the name of the entity."""
        return "Sodexo EcoPass amount"

    @property
    def unique_id(self) -> str:
        """Return the unique ID of the sensor."""
        return f"{DOMAIN}-{self._config[CONF_USERNAME]}-ECOPASS".lower()

    async def async_update(self) -> None:
        api = self._api

        try:
            account = await api.get_balance()
            self._state = account.eco_pass
            self._updated = True
            self._available = True

        except Exception as err:
            self._available = False
            _LOGGER.exception("Error updating data from DGEG API.", err)
