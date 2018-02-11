import json
import alexaHelper
import random
sentences = open("listOfSentences.txt").read().split("\n")


def createResponse(text):
	return {
			"version": "1.0",
			"sessionAttributes": {},
			"response": {
			"outputSpeech": {
			"type": "PlainText",
			"text": "Repeat the following sentence. {}".format(random.choice(sentences))
				},
				"shouldEndSession": False
			  }
			}


def lambda_handler(event, context):
	return createResponse("Ayyyyyyyyyyyyyyyyyyy")

def on_intent(intent_request, session):
	intent = intent_request["intent"]
	intent_name = intent_request["intent"]["name"]
	if intent_name == "startDiagnosis":
		return createResponse("Sup Bro")
	elif intent_name == 'aboutDev':
		return alexaHelper.devInfo()
	elif intent_name == "AMAZON.HelpIntent":
		return alexaHelper.get_welcome_response()
	elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
		return alexaHelper.handle_session_end_request()
