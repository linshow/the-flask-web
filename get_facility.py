import requests
import json
import time

api_key ='AIzaSyCKueW4v0pJNFNF5DMcNB52WPt-ScPpjjM'
def get_nearby_places(coordinates, business_type, next_page,count):
    global ano_count
    total_results = []
    URL = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='
		+coordinates+'&radius=500&key='+ api_key +'&type='
		+business_type+'&pagetoken='+next_page)
    r = requests.get(URL)
    response = r.text
    python_object = json.loads(response)
    results = python_object["results"]
    for result in results:
       
        
        place_name = result['name']
        total_results.extend([place_name])
        count +=1
        # print([business_type, place_name])
        
    # print(total_results)
    # print(len(total_results))
    while python_object.get("next_page_token"):
        next_page_token = python_object["next_page_token"]
        time.sleep(2)
        get_nearby_places(coordinates, business_type, next_page_token, count)
        total_results.extend([place_name])

        return
    
    ano_count = count
    return ano_count
    # print(ano_count)

# get_nearby_places([25.0271054,121.5694803],'parking', '',0)