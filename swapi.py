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
# Luiz Andrade - Refactored - 03/05/2023
################################
from sys import argv, exit
from requests import get
from math import floor
from convertHours import convertHours

#### Functions ####
# Generic function to get API response
def getResponse(urlAPI):
    response = get(urlAPI)
    if response.status_code == 200:
        global swapiReturn 
        swapiReturn = response.json()
        return swapiReturn
    else:
        print(f'Unexpect return: Status code {response.status_code}')
        exit(1)

# Work with starships informations in both pages
def locateStarships():
    if swapiReturn['results'] is not None:
        for __result in swapiReturn['results']:
            starshipName = __result['name']
            urlAPI = __result['url']
            starshipsReturn = getResponse(urlAPI)

            MGLT = starshipsReturn['result']['properties']['MGLT']
            consumables = starshipsReturn['result']['properties']['consumables']

            print(f'{starshipName} : {calculateStops(consumables, MGLT)}')
    else:
        return

# Calculates the number of stops
def calculateStops(consumables, MGLT):
    if MGLT != 'unknown':
        MGLT_hour = (int(travelDistance)/int(MGLT))
        travelStops = floor(MGLT_hour/convertHours(consumables))
        return travelStops
    else:
        travelStops = (f'Unknown stops | MGLT {MGLT} | Consumables: {consumables}')
        return travelStops

#### Start of code ####
# Check if has argument to travel distance or if needed manual input
if len(argv) > 1:
    travelDistance = argv[1]
    if not travelDistance.isnumeric():
        print('Please, use only numbers on next execution')
        exit(1)
else:
    travelDistance = input('Insert travel distance: ')
    while not travelDistance.isnumeric():
        print('Please, use only numbers')
        travelDistance = input('Insert travel distance: ')

urlAPI = 'https://www.swapi.tech/api/starships/'
getResponse(urlAPI)

# Search the URL of next page if exists
nextURL = [urlAPI]
for __nextURL in swapiReturn:
    if swapiReturn['next'] is not None:
        urlAPI = swapiReturn['next']
        nextURL.append(swapiReturn['next'])
        getResponse(urlAPI)

# Makes all this works using the starships pages
for starshipsPages in nextURL:
    locateStarships()
    urlAPI = starshipsPages
    getResponse(urlAPI)
