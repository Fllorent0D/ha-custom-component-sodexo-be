from typing import Dict

DOMAIN = "sodexo"
PLATFORM = "sensor"
DOMAIN_DATA = f"{DOMAIN}_data"

DEFAULT_ICON = "mdi:credit-card"
UNIT_OF_MEASUREMENT = "€"

ATTRIBUTION = "Data provided by https://users.pluxee.be"
LOGIN_URL = "https://users.pluxee.be"

LUNCH_PASS_SELECTOR = "body > header > div.header-fixed > div.balance-block > div > ul > li.lunch-pass > a > span.balance_price"
ECO_PASS_SELECTOR = "body > header > div.header-fixed > div.balance-block > div > ul > li.eco-pass > a > span.balance_price"
GIFT_PASS_SELECTOR = "body > header > div.header-fixed > div.balance-block > div > ul > li.cadeau-pass > a > span.balance_price"

COUNTRY_BE = "Belgium"

CONF_COUNTRY = "country"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"

CONF_COUNTRIES = [
    "Australia",
    COUNTRY_BE,
    "Brasil",
    "Canada",
    "Chile",
    "China",
    "Colombia",
    "Czech Republic",
    "Denmark",
    "Finland",
    "France",
    "India",
    "Indonesia",
    "Ireland",
    "Israel",
    "Italy",
    "Malaysia",
    "Mexico",
    "Middle East",
    "Netherlands",
    "Norway",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Qatar",
    "Romania",
    "Singapore",
    "South Africa",
    "South Korea",
    "Spain",
    "Sweden",
    "Switzerland",
    "Thailand",
    "Turkey",
    "United Arab Emirates",
    "United States",
    "United-Kingdom",
    "Vietnam"
]