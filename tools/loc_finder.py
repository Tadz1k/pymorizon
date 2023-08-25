from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="pymorizonv2", timeout=200)


def get_location(address):
    location = geolocator.geocode(f"{address}")
    return location

def get_url_location(address):
    if 'ulica' in address:
        address = address.replace('ulica', '')
    if 'ul' in address:
        address = address.replace('ul', '')
    if 'ul.' in address:
        address = address.replace('ul.', '')
    if ':' in address:
        address = address.replace(':', '')

    location = get_location(address)
    if location is None:
        return None
    data = str(location).split(',')
    if 'gmina' not in str(location):
        return f'/{data[0]}'
    else:
        data1 = data[2]
        if data1.startswith(' '):
            data1 = data1[1:]
        if data1.endswith(' '):
            data1 = data1[:-1]
        data1 = data1.replace('powiat ', '')
        return f'/{data1}/{data[0]}'
        
