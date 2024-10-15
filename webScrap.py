import requests
from bs4 import BeautifulSoup

# URL de la página a examinar
url = 'https://www.nombrerutyfirma.com/'

# Realizar la solicitud GET a la página
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Parsear el contenido HTML de la página
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar y extraer los datos que te interesan
    # Por ejemplo, encontrar todos los elementos <a> que contienen enlaces
    links = soup.find_all('a')
    
    # Mostrar los enlaces encontrados
    for link in links:
        print(link.get('href'))

else:
    print('Error al cargar la página:', response.status_code)