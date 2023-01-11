# Look up the location using the geolocator
location = geolocator.geocode(location_name)

# Return the latitude and longitude of the location
return (location.latitude, location.longitude)
