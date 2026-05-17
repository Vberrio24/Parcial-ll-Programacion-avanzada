import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout


BASE = "https://restcountries.com/v3.1"


class Country:
    def __init__(self, data: dict):
        self.name = data["name"]["common"]
        self.capital = data.get("capital", ["Sin capital"])[0]
        self.population = data.get("population", 0)
        self.area = data.get("area", 0)
        self.region = data.get("region", "Sin region")

    def __str__(self) -> str:
        return (
            f"{self.name} ({self.region})\n"
            f"  Capital: {self.capital}\n"
            f"  Poblacion: {self.population:,}\n"
            f"  Area: {self.area:,.2f} km2\n"
            f"  Densidad: {self.density():.2f} hab/km2"
        )

    def density(self) -> float:
        if self.area == 0:
            return 0
        return self.population / self.area

    def comparar(self, otros: list["Country"]) -> None:
        paises = [self] + otros

        print("Pais                 Poblacion        Area       Densidad")
        print("-" * 60)

        for pais in paises:
            print(
                f"{pais.name:18} "
                f"{pais.population:12,} "
                f"{pais.area:11,.0f} "
                f"{pais.density():10.2f} hab/km2"
            )

        mayor_poblacion = max(paises, key=lambda pais: pais.population)
        mayor_area = max(paises, key=lambda pais: pais.area)
        mayor_densidad = max(paises, key=lambda pais: pais.density())

        print("-" * 60)
        print(f"Mayor poblacion: {mayor_poblacion.name}")
        print(f"Mayor area: {mayor_area.name}")
        print(f"Mayor densidad: {mayor_densidad.name}")


class CountryAPI:
    def by_name(self, name: str) -> Country | None:
        url = f"{BASE}/name/{name}"

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return Country(response.json()[0])
        except Timeout:
            print(f"La API tardo demasiado buscando {name}.")
        except ConnectionError:
            print("No hay conexion a internet.")
        except HTTPError as error:
            status = error.response.status_code
            print(f"No se encontro el pais {name}. Codigo: {status}")

        return None

    def by_region(self, region: str) -> list[Country]:
        url = f"{BASE}/region/{region}"

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            return [Country(pais) for pais in data]
        except Timeout:
            print(f"La API tardo demasiado buscando la region {region}.")
        except ConnectionError:
            print("No hay conexion a internet.")
        except HTTPError as error:
            status = error.response.status_code
            print(f"No se encontro la region {region}. Codigo: {status}")

        return []