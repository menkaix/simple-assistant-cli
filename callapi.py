import requests
import json

def post_prompt(base_url, api_key, file_path, history, prompt) :

    response_history = []
    response = {}
    response_message = {}

    url = base_url+"?key="+api_key

    response_message['content'] = prompt ;
    response_message['role'] = "gemini"

    response['history'] = response_history
    response['message'] = response_message

    return response