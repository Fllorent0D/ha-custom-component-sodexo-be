"""Deprecated: Sodexo has been renamed to Pluxee. Please remove this integration and install Pluxee instead."""

import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the deprecated Sodexo integration."""
    _LOGGER.warning(
        "The Sodexo integration has been renamed to Pluxee. "
        "Please remove this integration and install Pluxee instead."
    )
    hass.components.persistent_notification.async_create(
        "The Sodexo integration has been renamed to **Pluxee**. "
        "Please remove Sodexo from HACS and install the new Pluxee integration.",
        title="Sodexo → Pluxee",
        notification_id="sodexo_deprecated",
    )
    return True
