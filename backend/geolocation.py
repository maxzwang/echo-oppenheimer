import googlemaps
import numpy as np

def get_loc():
    """Return the latitude, longitude, and error of the current location (currently given by IP address)"""
    gmaps = googlemaps.Client(key='AIzaSyD7X-bWmivYNzOHULVCHxJpuRxctXyAbeA')  # our client key
    curr_location = gmaps.geolocate()  # without any additional arguments, this just goes off of IP address
    est_lat, est_lng = curr_location['location'].values()
    est_error = curr_location['accuracy']  # the number of meters that google maps geolocation could be off by
    return est_lat, est_lng, est_error

def within_region():
  """ Return true if latitude and longitude are within a radius of the location we want to base our project at.
  Return false otherwise"""
  R_EARTH = 6378000 # meters
  R_PERIM = 2000  # meters
  lat_base = 40.3486419 #3273733   # set to be the center of East Pyne Hall
  lng_base = -74.6584222 #5707148

  est_lat, est_lng, est_error = get_loc()  # currently, using IP addresses, the error is ~3000 meters...

  lat_diff = est_lat - lat_base
  lng_diff = est_lng - lng_base
  y_dist = (np.abs(lat_diff) * np.pi / 180) * R_EARTH
  rad_at_lat = R_EARTH * np.cos(lat_base * np.pi / 180)
  x_dist = (np.abs(lng_diff) * np.pi / 180) * rad_at_lat
  dist_away = np.sqrt(x_dist**2 + y_dist**2)

  return dist_away < R_PERIM + est_error

def reverse_loc():
    """Reverse geolocate our position and return the address"""
    lat, lng, error = get_loc()
    gmaps = googlemaps.Client(key='AIzaSyD7X-bWmivYNzOHULVCHxJpuRxctXyAbeA')
    address_list_dict = gmaps.reverse_geocode((lat, lng)) #input tuple
    return address_list_dict[0]['formatted_address']


# print(get_loc())
# print(reverse_loc())
# print(within_region())
