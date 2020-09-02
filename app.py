from flask import Flask, render_template, request
import requests
import base64
import datetime

client_id = '2e2cc52be28c4a3dab756d2377edfe72'
client_secret = 'e75e32f16bed4482b97af54a4249ab94'

API_BASE_URL = 'https://api.spotify.com/'
token_url_get = 'https://accounts.spotify.com/authorize'


client_creds = f"{client_id}:{client_secret}"
client_creds_b64 = base64.b64encode(client_creds.encode()) 

token_url = 'https://accounts.spotify.com/api/token'
method = "POST"
token_data = {
  "grant_type": "client_credentials"
}

token_header = {
  "Authorization": f"Basic {client_creds_b64.decode()}"
}


response = requests.post(token_url, data=token_data, headers=token_header)
print(response.json())
valid_request = response.status_code in range(200, 299)

token_response_data = response.json()

if valid_request:
  now = datetime.datetime.now()
  access_token = token_response_data['access_token']
  expires_in = token_response_data['expires_in']
  expires = now + datetime.timedelta(seconds=expires_in)
  did_expire = expires < now
