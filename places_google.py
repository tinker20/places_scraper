from googleplaces import GooglePlaces, types, lang

YOUR_API_KEY = 'AIzaSyDytLuaLmy000d4VRakszHkhsjY5GKdiHA'

google_places = GooglePlaces(YOUR_API_KEY)

# You may prefer to use the text_search API, instead.
query_result = google_places.nearby_search(
        location='Garia, Kolkata', keyword='grocery',
        radius=20000, rankby='prominence', 
	types=[types.TYPE_GROCERY_OR_SUPERMARKET])

if query_result.has_attributions:
    print query_result.html_attributions


for place in query_result.places:
    # Returned places from a query are place summaries.
    print place.name
    print place.geo_location
    print place.reference

    # The following method has to make a further API call.
    place.get_details()
    # Referencing any of the attributes below, prior to making a call to
    # get_details() will raise a googleplaces.GooglePlacesAttributeError.
    print place.local_phone_number


# Adding and deleting a place