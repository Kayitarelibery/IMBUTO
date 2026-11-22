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
        return{
            "success": False,
            "error": "Weather information is unavailable for this location."
        }
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": coordinates["latitude"],
        "longitude": coordinates["longitude"],
        "current": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m",
        "timezone": "Africa/Kigali"
    }

    try: 
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        current = data["current"]
        return {
            "success": True,
            "location": location,
            "temperature": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "precipitation": current["precipitation"],
            "wind_speed": current["wind_speed_10m"],
            "time": current["time"]
        }
    except (requests.RequestException, KeyError, ValueError) as error:
        print(f"Weather API error: {error}")
        return{
            "success": False,
            "error": f"Unable to retrieve weather information. Please try again later."
        }