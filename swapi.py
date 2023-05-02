#        .---.  
#      .'_:___". 
#      |__ --==|
#      [  ]  :[| 
#      |__| I=[|   
#      / / ____|  
#     |-/.____.'   
#    /___\ /___\  
################################
# Luiz Andrade - Calculates stops needed with starships in space - 02/05/2023
################################
from sys import exit
import requests
from math import floor

# Function to get the starships information
def getResponse(urlAPI):
    response_swapi_url = requests.get(urlAPI)
    return response_swapi_url.json()

# Calculates how many stops are needed
def calcDistance():
    # The calc below gets the result rounded up (there are no 2.6 stops so we need only 2)
    travel_stops = floor(int(travel_distance)/int(MGLT))
    return travel_stops

# Get URLs of all starships
response_swapi = requests.get('https://www.swapi.tech/api/starships/')
if response_swapi.status_code == 200:
    starships_info = response_swapi.json()
else:
    print(f'Unexpect return: Status code {response_swapi.status_code}')
    exit(1)

# Numeric validation for travel distance
travel_distance = input("Insert travel distance: ")
while not travel_distance.isnumeric():
    print("Please, use only numbers")
    travel_distance = input("Insert travel distance: ")

print('STARSHIP MODEL: STOPS NEEDED')

# Get specific information about each starship 
for __result in starships_info['results']:
    urlAPI = __result['url']
    starships_return = getResponse(urlAPI)

    # Saving model and MGLT from each starship
    model = starships_return['result']['properties']['model']
    MGLT = starships_return['result']['properties']['MGLT']

    print(f'{model} : {calcDistance()}')
