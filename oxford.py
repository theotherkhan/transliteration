# -*- coding: utf-8 -*-

import json
import requests
app_id  = "d6d3e876"
app_key  = "ad726618038384c318a4582ff010950f"
endpoint = "entries"
language_code = "ur"
word_id = "amor"

#url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower()

api_base_url = 'https://od-api.oxforddictionaries.com/api/v2/entries/'
source_language = 'es'
target_language = 'en'
#word_id = requests.form['urduword']

url = api_base_url + source_language + '/' + word_id.lower() + '/translations=' + target_language

print url

r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})


#print("code {}\n".format(r.status_code))
print("text \n" + r.text)
#print("json \n" + json.dumps(r.json()))
