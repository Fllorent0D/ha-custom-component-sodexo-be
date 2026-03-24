![GitHub](https://img.shields.io/github/license/netsoft-ruidias/ha-custom-component-sodexo?style=for-the-badge)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/netsoft-ruidias/ha-custom-component-sodexo?style=for-the-badge)
![GitHub Release Date](https://img.shields.io/github/release-date/netsoft-ruidias/ha-custom-component-sodexo?style=for-the-badge)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/netsoft-ruidias/ha-custom-component-sodexo?style=for-the-badge)

# Belgian Sodexo Card Integration
Sodexo - Custom Component for Home Assistant

The data source for this integration is the [Sodexo/Pluxee](https://users.pluxee.be).

The author of this project categorically rejects any and all responsibility for the card balance and other data that were presented by the integration.

# Installation
## HACS (Recommended)
This is an official HACS integration and can be added via HACS.

Assuming you have already installed and configured HACS, follow these steps:

1. Navigate to the HACS integrations page
2. Choose Integrations under HACS
3. Click the '+' button on the bottom of the page
4. Serch for "Sodexo", choose it, and click install in HACS
5. Ready! Now continue with the configuration.

# Configuration

## Through the interface
1. Navigate to `Settings > Devices & Services` and then click `Add Integration`
2. Search for `Sodexo`
4. Enter your credentials
5. Repeat the procedure as many times as desired to include other cards you may have

## Sample Card

This is a sample card that displays the balance, last sensor update and last available balance date.

As a bonus, this sample also includes a `tap_action` to update the card's balance each time the card is pressed or clicked.

```yaml
type: entities
entities:
  - entity: sensor.sodexo_lunch_amount
    secondary_info: last-updated
    tap_action:
      action: call-service
      service: homeassistant.update_entity
      target:
        entity_id: sensor.sodexo_lunch_amount
  - entity: sensor.sodexo_lunch_amount
    name: Updated
    type: attribute
    attribute: updated
```

# Legal notice
This is a personal project and isn't in any way affiliated with, sponsored or endorsed by [Sodexo Belgium](https://users.pluxee.be).

All product names, trademarks and registered trademarks in (the images in) this repository, are property of their respective owners. All images in this repository are used by the project for identification purposes only.

