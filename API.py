import requests
from pydantic import BaseModel, ValidationError


class CurrentBase(BaseModel):
    time: str
    temperature_2m: float


class DataModel(BaseModel):
    latitude: float
    longitude: float
    current: CurrentBase


def get_weather(latitude, longitude):
    parametry = {
        "latitude": latitude,  # Paris latitude
        "longitude": longitude,  # Paris longitude
        "current": "temperature_2m",
    }

    url = "https://api.open-meteo.com/v1/forecast/"

    response = requests.get(url, params=parametry)
    data = response.json()
    return data


miasta = {
    "Londyn": get_weather(51.50, -0.12),
    "Paryz": get_weather(48.85, 2.35),
    "Tokio": get_weather(35.68, 139.69),
}

for nazwa_miasta, dane_miasta in miasta.items():
    try:
        temperatura = DataModel.model_validate(dane_miasta)
        print("Walidacja poprawna")
        print(
            f"Tutaj jest temperatura z {nazwa_miasta} o którą prosiłeś: Współrzędne {temperatura.latitude}, {temperatura.longitude} - Temperatura: {temperatura.current.temperature_2m} stopni Celsjusza o godzinie {temperatura.current.time}"
        )
    except ValidationError as e:
        print(f"Wystąpił Błąd! {e}")
