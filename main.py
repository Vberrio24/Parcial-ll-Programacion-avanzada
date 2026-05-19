from country import Country, CountryAPI


def cargar_paises(api: CountryAPI, elecciones: dict[str, str]) -> list[Country]:
    paises = []

    for letra, pais_nombre in elecciones.items():
        pais = api.by_name(pais_nombre)
        if pais is not None:
            print(f"{letra.upper()} -> {pais.name}")
            paises.append(pais)

    return paises


def main() -> None:
    api = CountryAPI()

    victor = {
        "v": "venezuela",
        "i": "india",
        "c": "colombia",
        "t": "turkey",
        "o": "oman",
        "r": "romania",
    }

    jorge = {
        "j": "japan",
        "o": "oman",
        "r": "rwanda",
        "g": "germany",
        "e": "egypt",
    }

    print("Paises de Victor")
    paises_victor = cargar_paises(api, victor)

    print("\nPaises de Jorge")
    paises_jorge = cargar_paises(api, jorge)

    paises = paises_victor + paises_jorge

    print("\nDatos de los paises\n")
    for pais in paises:
        print(pais)
        print()

    print("Comparacion general\n")
    if paises:
        primero = paises[0]
        primero.comparar(paises[1:])


if __name__ == "__main__":
    main()