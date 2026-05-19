## Parcial Programacion Avanzada - POO + API
Integrantes
- Victor Andrés Berrio Huertas
- Jorge Mario Escudero Castañeda

# Descripcion
Este proyecto consulta informacion de paises usando la API publica REST Countries.

La solucion fue desarrollada con Programacion Orientada a Objetos. Cada letra de los nombres Victor y Jorge se asocia con un pais consultado desde la API. Luego se comparan los paises por poblacion, area y densidad poblacional.

# API usada
REST Countries:

https://restcountries.com/v3.1

# Endpoints usados:

- Buscar por nombre exacto: /name/{name}?fullText=true
- Buscar por region: /region/{region}

# Clases

# Country
Representa un pais como objeto.

# Atributos:

- name: nombre comun del pais.
- capital: capital del pais.
- population: poblacion total.
- area: area del pais en km2.
- region: region o continente.

# Metodos:

__init__(self, data): recibe el diccionario de la API y guarda los datos principales del pais.
__str__(self): devuelve una cadena legible con la informacion del pais.
- density(self): calcula la densidad poblacional dividiendo poblacion entre area.
- comparar(self, otros): compara el pais actual con otros paises e imprime una tabla comparativa.

# CountryAPI
Se encarga de hacer las peticiones a la API.

# Metodos:

- by_name(self, name): busca un pais por nombre y devuelve un objeto Country.
- by_region(self, region): busca paises por region y devuelve una lista de objetos Country.

# Paises elegidos
# Victor
- V: Venezuela
- I: India
- C: Colombia
- T: Turkey
- O: Oman
- R: Romania
# Jorge
- J: Japan
- O: Oman
- R: Rwanda
- G: Germany
- E: Egypt
- Nota: Oman se usa en ambos nombres porque la letra O aparece en Victor y en Jorge y es el único paí con O.

# Archivos
- country.py: contiene las clases Country y CountryAPI.
- main.py: contiene el programa principal.
- requirements.txt: contiene la dependencia requests.

# Como ejecutar
- Instalar la libreria necesaria:

- pip install -r requirements.txt

# Ejecutar el programa:

- python main.py

# El programa muestra:

- Pais elegido por cada letra.
- Capital.
- Region.
- Poblacion.
- Area.
- Densidad poblacional.
- Tabla comparativa.
- Pais con mayor poblacion.
- Pais con mayor area.
- Pais con mayor densidad
