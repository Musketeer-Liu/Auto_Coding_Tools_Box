# python3 --> Enter Python Shell
# from geocode import getGeocodeLocation
# getGeocodeLocation("Place you wanto to query")


import httplib2
import json


def getGeocodeLocation(inputString):
    google_api_key = "AIzaSyDZHGnbFkjZcOEgYPpDqlO2YhBHKsNxhnE"
    locatationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'%(locatationString, google_api_key))

    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)

    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    # print(latitude, longitude)
    return (latitude, longitude)

    # print("response header: %s \n \n" % response)
    # return result

# san_francisco = getGeocodeLocation("San Francisco, CA")
# response header: {'content-type': 'application/json; charset=UTF-8', 'date': 'Sat, 27 Jan 2018 06:25:35 GMT', 'expires': 'Sun, 28 Jan 2018 06:25:35 GMT', 'cache-control': 'public, max-age=86400', 'vary': 'Accept-Language', 'access-control-allow-origin': '*', 'server': 'mafe', 'content-length': '1749', 'x-xss-protection': '1; mode=block', 'x-frame-options': 'SAMEORIGIN', 'alt-svc': 'hq=":443"; ma=2592000; quic=51303431; quic=51303339; quic=51303338; quic=51303337; quic=51303335,quic=":443"; ma=2592000; v="41,39,38,37,35"', 'status': '200', '-content-encoding': 'gzip', 'content-location': 'https://maps.googleapis.com/maps/api/geocode/json?address=San+Francisco,+CA&key=AIzaSyDZHGnbFkjZcOEgYPpDqlO2YhBHKsNxhnE'}

# san_francisco
# {'results': [{'address_components': [{'long_name': 'San Francisco', 'short_name': 'SF', 'types': ['locality', 'political']}, {'long_name': 'San Francisco County', 'short_name': 'San Francisco County', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'California', 'short_name': 'CA', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'United States', 'short_name': 'US', 'types': ['country', 'political']}], 'formatted_address': 'San Francisco, CA, USA', 'geometry': {'bounds': {'northeast': {'lat': 37.9298239, 'lng': -122.28178}, 'southwest': {'lat': 37.6398299, 'lng': -123.173825}}, 'location': {'lat': 37.7749295, 'lng': -122.4194155}, 'location_type': 'APPROXIMATE', 'viewport': {'northeast': {'lat': 37.812,'lng': -122.3482}, 'southwest': {'lat': 37.70339999999999, 'lng': -122.527}}}, 'place_id': 'ChIJIQBpAG2ahYAR_6128GcTUEo', 'types': ['locality', 'political']}], 'status': 'OK'}

# san_francisco.keys()
# dict_keys(['results', 'status'])

# san_francisco['results'][0]['geometry']['location']['lat']
# 37.7749295

# san_francisco['results'][0]['geometry']['location']['lng']
# -122.4194155
