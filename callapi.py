import requests
import json

def post_prompt(base_url, api_key, file_path, history, prompt) :

    response_history = []
    response = {}
    response_message = {}
    payload = {}


    url = base_url+"?key="+api_key

    payload["history"]= history
    payload["path"]=file_path
    payload["prompt"]=prompt

    json_payload = json.dumps(payload)
    headers = {
        'Content-Type':'application/json'
    }

    api_response=requests.request("POST", url, headers=headers, data=json_payload)

    response = json.loads(api_response.text)

    return response