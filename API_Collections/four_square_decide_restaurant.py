from geocode import getGeocodeLocation
import json
import httplib2

import sys
import codecs

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = ""
foursquare_client_secret = ""

def decide_restaurant(mealType, location):
    # Call getGeocodeLocation to get latitude and longitude of the location_type
    latitude, longitude = geocode.getGeocodeLocation(location)

    # Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings
    url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20170801&ll=%s,%s&query=%s' % (foursquare_client_id, foursquare_client_secret, latitude, longitude, mealType))
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])


    if result['response']['venues']:
        # Grab the first restaurant
        restaurant = result['response']['venues'][0]
        venue_id = restaurant['id']
        restaurant_name = restaurant['name']
        restaurant_address = restaurant['location']['formattedAddress']
        # Format the formatted address into a single line
        address_line = ""
        for i in restaurant_address:
            address_line += i + " "
        restaurant_address = address_line

        # Get a  300x300 picture of the restaurant using the venue_id (change the dimension if necessary)
        url = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&client_secret=%s&v=20170815' % (venue_id, foursquare_client_id, foursquare_client_secret))
        result = json.loads(h.request(url, 'GET')[1])
        if result['response']['photos']['items']:
            # Grab the first picture
            first_picture = result['response']['photos']['items'][0]
            prefix = first_picture['prefix']
            suffix = first_picture['suffix']
            image_url = prefix + "300x300" + suffix
        else:
            # If no image is available, use the default url
            image_url = 'https://goo.gl/uGibii'

        # Return a dictionary contianing the restaurant name, address, and image url
        restaurant_info = {
            'name': restaurant_name,
            'address': restaurant_address,
            'image': image_url
        }

        print('Restaurant Name: %s' % restaurant_info['name'])
        print('Restaurant Address: %s' % restaurant_info['address'])
        print('Restaurant Image: %s \n' % restaurant_info['image'])

        return restaurant_info

    else:
        print("No Restaurant Found for %s" % location)
        return "No Restaurant Found"


if __name__ == '__main__':
    decide_restaurant("Pizza", "Tokyo, Japan")
    decide_restaurant("Tacos", "Jakarta, Indonesia")
    decide_restaurant("Tpas", "Maputo, Mozambique")
    decide_restaurant("Falafel", "Cairo, Egypt")
    decide_restaurant("Spaghetti", "New Delhi, India")
    decide_restaurant("Cappuccino", "Geneva, Switzerland")
    decide_restaurant("Sushi", "Los Angeles, California")
    decide_restaurant("Steak", "La Paz, Bolivia")
    decide_restaurant("Gyros", "Sydney, Australia")
