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
from sys import argv, exit
from calc import convertHours
import requests
from math import floor

# Function to get the starships information
def getResponse(urlAPI):
    response_swapi_url = requests.get(urlAPI)
    return response_swapi_url.json()

# Get URLs of all starships
response_swapi = requests.get('https://www.swapi.tech/api/starships/')
if response_swapi.status_code == 200:
    starships_info = response_swapi.json()
else:
    print(f'Unexpect return: Status code {response_swapi.status_code}')
    exit(1)

# Calculates how many stops are needed
def calcStops():
    # The calc below gets the result rounded up (there are no 2.6 stops so we need only 2)
    MGLT_hour = (int(travel_distance)/int(MGLT))
    travel_stops = floor(MGLT_hour/convertHours(consumables))
    return travel_stops

# Numeric validation for travel distance
if len(argv) > 1:
    travel_distance = argv[1]
    if not travel_distance.isnumeric():
        print('Please, use only numbers on next execution')
        exit(1)
else:
    travel_distance = input('Insert travel distance: ')
    while not travel_distance.isnumeric():
        print('Please, use only numbers')
        travel_distance = input('Insert travel distance: ')

# Get specific information about each starship 
for __result in starships_info['results']:
    starship_name = __result['name']
    urlAPI = __result['url']
    starships_return = getResponse(urlAPI)

    # Saving model and MGLT from each starship
    MGLT = starships_return['result']['properties']['MGLT']
    consumables = starships_return['result']['properties']['consumables']

    print(f'{starship_name} : {calcStops()}')
