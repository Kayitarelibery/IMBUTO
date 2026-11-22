import requests

LOCATIONS = {
    "Kigali": {"latitude": -1.9441, "longitude": 30.0619},
    "Huye": {"latitude": -2.5967, "longitude": 29.7394},
    "Musanze": {"latitude": -1.4998, "longitude": 29.6349},
    "Rubavu": {"latitude": -1.6792, "longitude": 29.2633},
    "Rwamagana": {"latitude": -1.9487, "longitude": 30.4347},
    "Muhanga": {"latitude": -2.0845, "longitude": 29.7520}
}


def get_weather(location):
    coordinates = LOCATIONS.get(location)

    if not coordinates:
        return {
            "success": False,
            "error": "Weather information is unavailable for this location."
        }

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": coordinates["latitude"],
        "longitude": coordinates["longitude"],
        "current": (
            "temperature_2m,relative_humidity_2m,"
            "precipitation,wind_speed_10m"
        ),
        "timezone": "Africa/Kigali"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        if not isinstance(data, dict):
            raise ValueError("Invalid API response")

        current = data.get("current")

        if not isinstance(current, dict):
            raise ValueError("Weather measurements are missing")

        required_fields = [
            "temperature_2m",
            "relative_humidity_2m",
            "precipitation",
            "wind_speed_10m",
            "time"
        ]

        if any(field not in current or current[field] is None
               for field in required_fields):
            raise ValueError("Incomplete weather information")

        return {
            "success": True,
            "location": location,
            "temperature": float(current["temperature_2m"]),
            "humidity": float(current["relative_humidity_2m"]),
            "precipitation": float(current["precipitation"]),
            "wind_speed": float(current["wind_speed_10m"]),
            "time": current["time"]
        }

    except requests.Timeout:
        return {
            "success": False,
            "error": "Weather service timed out. Please try again."
        }

    except requests.RequestException:
        return {
            "success": False,
            "error": "Weather service is temporarily unavailable."
        }

    except (ValueError, TypeError, KeyError):
        return {
            "success": False,
            "error": "Weather data could not be processed. Please try again."
        }
