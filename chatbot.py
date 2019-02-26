import json
from flask import Flask, request
from bot import Bot
import random



PAGE_ACCESS_TOKEN = 'EAAMGL1Nb3HsBAA4zAY685knfH1s60TkEsC5ru8gmZC0XyHsZAzMKfaWliu7XEZBgfh5VAFdbV4D1ujaZBnpxgwTvMRhyyiDwJZC8Rw30sBC8DpfvOKKcKbZB0idZBW5JpZCo5mudJ5lnujDZCyT5t9yKlicWtv3uBmdPVqxQSZBUT7eQZDZD'


GREETINGS = ['hi', 'hello', 'kamusta']

#QUESTIONS
ASKING_NAME = ['what is your name', 'what is your name?', 'What is your name', 'What is your name?']
ASKING_LOCATION = ['where you from?',
					'where you from',
					'Where You From',
					'Where You From?',
					'where are you?',
					'are you from?',
					'ur from?']

#OTHER INPUTS

INPUT_CONVO = ['Nice meeting you', 
				'nice meeting you :)',
				'Nice name :)',
				'nice name']

#ANSWER
app = Flask(__name__)
ra_aname = ["Hi there!  My name’s Crystel",
			"My Name is Crystel",
			"Oh by th way I'm Crystel",
			"I think I’ve seen you around, but we haven’t officially met.  I’m Crystel",
			"Have we met?  I’m Crystel"]

@app.route('/', methods=['GET', 'POST'])



def webhook():
	if request.method == 'GET':
		token = request.args.get('hub.verify_token')
		challenge = request.args.get('hub.challenge')

		if token == 'sercete':
			return str(challenge)
		return '400'

	else:
		print(request.data)
		data = json.loads(request.data)
		messaging_events = data ['entry'][0]['messaging']
		bot = Bot (PAGE_ACCESS_TOKEN)
		for message in messaging_events:
			user_id = message['sender']['id']
			text_input = message['message'].get('text')
			response_text = 'Im still learning  i cannot understand :( please ask new question :) '
			if text_input in GREETINGS:
				response_text = 'Hello:)'
			elif text_input in ASKING_NAME:
				response_text = random.choice(ra_aname)
			elif text_input in ASKING_LOCATION:
				response_text = "I'm from This Page :)"
			elif text_input in INPUT_CONVO:
				response_text = "Thank you : ) , By the way how can I assist You?"
				
			print('Message form user ID {} - {}'.format(user_id, text_input))
			bot.send_text_message(user_id, response_text)

		return '200'

if __name__ == '__main__':
	app.run(debug=True)

#https://www.youtube.com/watch?v=Y9zr2NWD028

