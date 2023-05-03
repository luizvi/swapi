from dateutil.parser import parse

# All the time was converted to hours to get the consumables in hours
def convertHours(consumables):
    timeUnit = {'year': 8760, 'years': 8760,
                'month': 720, 'months': 720,
                'week': 168, 'weeks': 168,
                'days': 24}
    consParts = consumables.split(' ')
    if len(consParts) == 2 and consParts[1] in timeUnit:
        timeHours = int(consParts[0]) * timeUnit[consParts[1]]
        return timeHours
    else:
        return None
