import googlemaps
import pandas as pd

# Replace YOUR_API_KEY with your actual API key
gmaps = googlemaps.Client(key='YOUR_API_KEY')

# Read the data from the CSV file
data = pd.read_csv('~/Documents/NAME_OF_THE_CSV.csv')

# Create empty lists for the address and geolocation data
addresses = []
latitudes = []
longitudes = []

# Loop through the data and retrieve the address and geolocation for each place name
for name in data['name/en-US']:
    try:
        # Get the address for the place name using Google Maps API
        geocode_result = gmaps.geocode(name)
        address = geocode_result[0]['formatted_address']
        latitude = geocode_result[0]['geometry']['location']['lat']
        longitude = geocode_result[0]['geometry']['location']['lng']
    except:
        # If the address and geolocation cannot be retrieved, set them to None
        address = None
        latitude = None
        longitude = None
    
    # Append the address and geolocation to the respective lists
    addresses.append(address)
    latitudes.append(latitude)
    longitudes.append(longitude)

# Add the address and geolocation data to the original data
data['address'] = addresses
data['latitude'] = latitudes
data['longitude'] = longitudes

# Save the data to a new CSV file
data.to_csv('~/Documents/NAME_OF_NEW_CSV.csv', index=False)
