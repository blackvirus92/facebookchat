import requests
import json

FACEBOOK_GRAPH_URL = 'https://graph.facebook.com/v2.6/me/'


class Bot(object):

	def __init__(self, access_token, api_url=FACEBOOK_GRAPH_URL):
		self.access_token = access_token
		self.api_url = api_url


	def send_text_message(self, psid, message, messaging_type="RESPONSE"):

		headers = {

			'Content-Type' : 'application/json'
		}


		data = {

			'messaging_type':messaging_type,
			'recipient':{'id': psid},
			'message':{'text': message}

		}


		params = {'access_token': self.access_token}
		self.api_url = self.api_url + 'messages'

		response = requests.post(self.api_url, 
								headers = headers, 
								params = params, 
								data= json.dumps(data))

		print (response.content)

bot = Bot('EAAMGL1Nb3HsBACkClaOmiFIUT5LZAlCAPPxB0fZAIfsmgUhEoC5YcloyvidD2kXyTEq3BYp1rWMq0KOZAtQZA381CbZAjzNbkHK7NxFExLgPBlNpteCepwONX3ImtRVQhiR7o9RaAhQHIb7v2D3iZAS03ZCa8rO4bUP0o8lCfqjdAZDZD')






