import json
from flask import Flask, request
from bot import Bot
import random
import wolframalpha
import wikipedia

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

import time



app_id ="XA7V4E-68QJHPX8R8"
client = wolframalpha.Client(app_id)

#stwiches


PAGE_ACCESS_TOKEN = 'EAAMGL1Nb3HsBAA4zAY685knfH1s60TkEsC5ru8gmZC0XyHsZAzMKfaWliu7XEZBgfh5VAFdbV4D1ujaZBnpxgwTvMRhyyiDwJZC8Rw30sBC8DpfvOKKcKbZB0idZBW5JpZCo5mudJ5lnujDZCyT5t9yKlicWtv3uBmdPVqxQSZBUT7eQZDZD'


GREETINGS = ['hi', 'hello', 'kamusta']

#QUESTIONS
ASKING_NAME = ['what is your name', 'what is your name?', 'What is your name', 'What is your name?',"whats your name"]
ASKING_LOCATION = ['where you from?',
					'where you from',
					'Where You From',
					'Where You From?',
					'where are you?',
					'are you from?',
					'ur from?']

ASKING_MY_LOCATION = ['Where am I?',
						'where am i?',
						'where am i', 
						'where i am?',
						'what is my location',
						'where iam',
						'where iam?']
SEND_EMAIL = "send email"

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
		data = json.loads(request.data.decode('utf-8'))
		messaging_events = data ['entry'][0]['messaging']
		bot = Bot (PAGE_ACCESS_TOKEN)
		for message in messaging_events:
			user_id = message['sender']['id']
			text_input = message['message'].get('text')

			try:

				#recieving "send email"
				seperator = text_input.split(", ")
				seprator_output = seperator[0]

	# Sending Email Filter

				SEND_MAIL_SYNTAX = text_input.split()
				OUTPUT_SYNTAX_SEND = SEND_MAIL_SYNTAX[0]
			except:
				pass
	



			try:
				res = client.query(text_input)
				response_text = next(res.results).text
			except:
				try:
					response_text = wikipedia.summary(text_input)
				except:
					response_text = "I Think I need To learn That"
					pass
				pass
			
			try:
				if text_input in GREETINGS:
					response_text = 'Hello:)'
				elif text_input in ASKING_NAME:
					response_text = random.choice(ra_aname)
				elif text_input in ASKING_LOCATION:
					response_text = "I'm from This Page :)"
				elif text_input in INPUT_CONVO:
					response_text = "Thank you : ) , By the way how can I assist You?"
				elif text_input in ASKING_MY_LOCATION:
					response_text = "I do not know Im still learning to locate you.. :)"
				elif seprator_output in "send email":
					response_text = 'Ok send send me the details. By typing "<sendto> <Reciepient E-mail>, <Subject>, <Message>  "' 
				elif OUTPUT_SYNTAX_SEND in "sendto":
					try:

						insyntax = text_input.split()
						insyntax2 = insyntax[1]
						insyntax3 = insyntax2.split(",")
						emailsyntax = insyntax3[0]

						subject_syntax = text_input.split(", ")
						subject_syntax2 = subject_syntax[1]

						message_syntax = text_input.split(", ")
						message_syntax2 = message_syntax[2]


						email_user = 'djaydequina92@gmail.com'
						email_password = 'Dequina761'
						email_send = str(emailsyntax)
						subject = str(subject_syntax2)

						msg = MIMEMultipart()
						msg['From'] = email_user
						msg['To'] = email_send
						msg['Subject'] = subject

						body = str(message_syntax2)
						msg.attach(MIMEText(body,'plain'))
						
						text = msg.as_string()
						server = smtplib.SMTP('smtp.gmail.com',587)
						server.starttls()
						server.login(email_user,email_password)


						server.sendmail(email_user,email_send,text)
						server.quit()
						response_text = 'The mail has been sent successfully ! :) <3'
					except:
						response_text = 'invalid sytax or email'
			except:
				pass
				

			bot.send_text_message(user_id, response_text)

		return '200'

if __name__ == '__main__':
	app.run(debug=True)

#https://www.youtube.com/watch?v=Y9zr2NWD028

