"""Sensor platform for Pluxee integration."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from pluxee import PluxeeBalance

from .const import CONF_USERNAME, DOMAIN
from .coordinator import PluxeeCoordinator

type PluxeeConfigEntry = __import__("homeassistant").config_entries.ConfigEntry[
    PluxeeCoordinator
]


@dataclass(frozen=True, kw_only=True)
class PluxeeSensorEntityDescription(SensorEntityDescription):
    """Describe a Pluxee sensor."""

    value_fn: Callable[[PluxeeBalance], float]


SENSORS: tuple[PluxeeSensorEntityDescription, ...] = (
    PluxeeSensorEntityDescription(
        key="lunch_pass",
        translation_key="lunch_pass",
        native_unit_of_measurement="€",
        device_class=SensorDeviceClass.MONETARY,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: data.lunch_pass,
    ),
    PluxeeSensorEntityDescription(
        key="eco_pass",
        translation_key="eco_pass",
        native_unit_of_measurement="€",
        device_class=SensorDeviceClass.MONETARY,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: data.eco_pass,
    ),
    PluxeeSensorEntityDescription(
        key="gift_pass",
        translation_key="gift_pass",
        native_unit_of_measurement="€",
        device_class=SensorDeviceClass.MONETARY,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: data.gift_pass,
    ),
    PluxeeSensorEntityDescription(
        key="conso_pass",
        translation_key="conso_pass",
        native_unit_of_measurement="€",
        device_class=SensorDeviceClass.MONETARY,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda data: data.conso_pass,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: PluxeeConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Pluxee sensors from a config entry."""
    coordinator = entry.runtime_data
    username = entry.data[CONF_USERNAME]

    async_add_entities(
        PluxeeSensor(coordinator, description, username) for description in SENSORS
    )


class PluxeeSensor(CoordinatorEntity[PluxeeCoordinator], SensorEntity):
    """Representation of a Pluxee balance sensor."""

    entity_description: PluxeeSensorEntityDescription
    _attr_has_entity_name = True
    _attr_attribution = "Data provided by Pluxee"
    _attr_icon = "mdi:credit-card"

    def __init__(
        self,
        coordinator: PluxeeCoordinator,
        description: PluxeeSensorEntityDescription,
        username: str,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self.entity_description = description
        self._attr_unique_id = f"{DOMAIN}-{username}-{description.key}".lower()
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, username)},
            name=f"Pluxee {username}",
            manufacturer="Pluxee",
            entry_type=DeviceEntryType.SERVICE,
            configuration_url="https://users.pluxee.be",
        )

    @property
    def native_value(self) -> float | None:
        """Return the sensor value."""
        if self.coordinator.data is None:
            return None
        return self.entity_description.value_fn(self.coordinator.data)
