"""Config flow for Pluxee integration."""

from __future__ import annotations

import asyncio
import logging

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.helpers import config_validation as cv
from pluxee import PluxeeAsyncClient, PluxeeLoginError

from .const import CONF_PASSWORD, CONF_USERNAME, DOMAIN

_LOGGER = logging.getLogger(__name__)

DATA_SCHEMA = vol.Schema(
    {vol.Required(CONF_USERNAME): cv.string, vol.Required(CONF_PASSWORD): cv.string}
)


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Pluxee config flow."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user interface."""
        errors = {}

        if user_input is not None:
            await self.async_set_unique_id(user_input[CONF_USERNAME].lower())
            self._abort_if_unique_id_configured()

            if await self._test_credentials(user_input):
                return self.async_create_entry(
                    title=f"Pluxee {user_input[CONF_USERNAME]}",
                    data=user_input,
                )
            errors = {"base": "auth"}

        return self.async_show_form(
            step_id="user",
            data_schema=DATA_SCHEMA,
            errors=errors,
        )

    async def _test_credentials(self, user_input: dict) -> bool:
        """Return true if credentials are valid."""
        try:
            async with asyncio.timeout(10):
                api = PluxeeAsyncClient(
                    user_input[CONF_USERNAME], user_input[CONF_PASSWORD]
                )
                await api.get_balance()
                return True
        except PluxeeLoginError:
            return False
        except Exception:
            _LOGGER.exception("Unexpected error during credential validation")
            return False
