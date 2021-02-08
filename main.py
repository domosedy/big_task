import requests


def get_picture(url, spn, x, y, map_file):
    params = {
        'll': str(x) + ',' + str(y)
        'spn': spn,
        'l': 'sat',
        'apikey': '40d1649f-0493-4b70-98ba-98533de7710b'
    }

    response = requests.get(url, params=params)
    with open(map_file, 'w') as f:
        f.write(response.content)


def get_coords(name_of_object):
    url = 'http://geocode-maps.yandex.ru/1.x/'
    params = {
        'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
        'format': 'json',
        'geocode': name_of_object
    }

    response = requests.get(url, params=params).json()
    toponym = response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    x, y = [float(i) for i in toponym["Point"]['pos'].split()]
    return x, y
