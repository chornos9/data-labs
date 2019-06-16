import requests
from pprint import pprint
from bs4 import BeautifulSoup

METRO_MADRID_ROOT_URL = "https://www.metromadrid.es"
METRO_MADRID = METRO_MADRID_ROOT_URL + "/es"

response = requests.get(METRO_MADRID)
soup = BeautifulSoup(response.text, "html.parser")

lines_container = soup.find("ul", {'class': 'list__otraslineas'}) #find para buscar solo 1 elemento
lines = lines_container.find_all("a", {'role': 'link'}) #find_all para buscar todos

lines_href = [line.get('href') for line in lines] #href = hiperlink_reference

#pprint(lines)

for line_href in lines_href:
    line_href = METRO_MADRID_ROOT_URL + line_href
    print(line_href)

    # numero de linea
    response = requests.get(line_href)
    soup = BeautifulSoup(response.text, "html.parser")
    numero_linea = soup.find("span", {'class': 'text-line'}) #find para buscar solo 1 elemento
    pprint(numero_linea.text.strip())

    # estaciones
    nombres_estacion = soup.find_all("p", {'class': 'list-line__btn__text'}) #find para buscar solo 1 elemento
    stops = [nombre_estacion.text for nombre_estacion in nombres_estacion]
    print(stops)

