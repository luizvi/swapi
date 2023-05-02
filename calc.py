import re

# Convert every time notation to hours
def convertHours(consumables):
    time_value = int(re.findall(r'\d+', consumables)[0])
#    print('TIME VALUE', time_value)
    time_unit = re.sub(r"\d+", "", consumables)
#    print('INFORMACAO:::::::: ', time_value, time_unit)
    if time_unit == ' days':
        return time_value * 24
    elif time_unit == ' week' or time_unit == ' weeks':
        return time_value * 24 * 7
    elif time_unit == ' month' or time_unit == ' months':
        return time_value * 24 * 30
    elif time_unit == ' years' or time_unit == ' year':
        return time_value * 24 * 365
    else:
        print(f'eRRO: {time_unit} - {time_value}')
