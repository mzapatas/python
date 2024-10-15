import requests
from bs4 import BeautifulSoup

url = 'https://www.nombrerutyfirma.com/'

search_term = input("Ingrese el nombre a buscar: ")

response = requests.get(url + '#apellido' + search_term) 
soup = BeautifulSoup(response.text, 'html.parser')

results = soup.find_all('h3', class_='font-weight-bold')

print(f"Resultados para la búsqueda: {search_term}")
for result in results:
    print(result.text)
    print('-'*50)