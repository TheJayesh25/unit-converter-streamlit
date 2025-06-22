from dotenv import load_dotenv
from typing import Union
import requests
import os

load_dotenv()

def convert_currency(value: float, from_unit: str, to_unit: str) -> Union[float, str]:
    """Converts currency from one unit to another using ExchangeRate API."""
    from_unit = from_unit.upper().strip()
    to_unit = to_unit.upper().strip()

    try:
        API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_unit}"
        response = requests.get(url, timeout=5)

        response.raise_for_status()  # Raises HTTPError for bad status codes

        data = response.json()
        conversion_rate = data["conversion_rates"].get(to_unit)

        if conversion_rate is None:
            return f"Sorry, currency code '{to_unit}' not supported."

        return round(value * conversion_rate, 6)

    except requests.exceptions.RequestException as e:
        return f"Network error: {e}"
    except KeyError:
        return "Unexpected response format from currency API."
    except Exception as e:
        return f"Something went wrong: {e}"