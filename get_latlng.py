import pymysql
import googlemaps




def get_latlng(address):
    latitude=[]
    longitude=[]
    new_latlng=[]
    global new_address
    gmaps = googlemaps.Client(key='AIzaSyCKueW4v0pJNFNF5DMcNB52WPt-ScPpjjM')

    geocode_result = gmaps.geocode(address)
    if geocode_result:
            latitude = geocode_result[0]['geometry']['location']['lat']
            longitude = geocode_result[0]['geometry']['location']['lng']
    else:
        latitude = ["None"]
        longitude = ["None"]
    new_latlng.append(latitude)
    new_latlng.append(longitude)
    # new_latlng ="'" + latitude + "," + longitude+"'"
    # print(new_address)
    return new_latlng

# print(get_latlng("臺北市北投區石牌路2段335號"))


