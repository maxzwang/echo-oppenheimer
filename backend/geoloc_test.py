from geolocation import get_loc, reverse_loc, within_region

print("Your current location (using your IP address):" + str(get_loc()))
print("Your current address: " + str(reverse_loc()))
print("You are within 2000 meters of East Pyne: " + str(within_region()))