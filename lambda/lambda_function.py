import json
import alexaHelper
import random
sentences = open("listOfSentences.txt").read().split("\n")
SKILLNAME = "Alexa Speech Diagnostic Tool"
INITIALSPEECH = "Thank you for checking out the alexa speech diagnostic tool.  We can detect early onset childhood speech disorders"
REPEATSPEECH = INITIALSPEECH

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
	if event["request"]["type"] == "LaunchRequest":
		return alexaHelper.get_welcome_response(SKILLNAME, INITIALSPEECH, REPEATSPEECH)
	elif event["request"]["type"] == "IntentRequest":
		return on_intent(event["request"], event["session"])

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
