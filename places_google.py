from googleplaces import GooglePlaces, types, lang

YOUR_API_KEY = 'AIzaSyDytLuaLmy000d4VRakszHkhsjY5GKdiHA'

google_places = GooglePlaces(YOUR_API_KEY)

# You may prefer to use the text_search API, instead.
query_result = google_places.text_search(
        query='shops in Mumbai', 
	types=[types.TYPE_LODGING])

for place in query_result.places:
    # Returned places from a query are place summaries.
    print place.name
    print place.geo_location

    # The following method has to make a further API call.
    place.get_details()
    # Referencing any of the attributes below, prior to making a call to
    # get_details() will raise a googleplaces.GooglePlacesAttributeError.
    print place.local_phone_number


# Adding and deleting a place
