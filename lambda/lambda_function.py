import json



def createResponse(text):
	return {
			"version": "1.0",
			"sessionAttributes": {},
			"response": {
			"outputSpeech": {
			"type": "PlainText",
			"text": "Thank you for using Diagnostic app that I can't think of a name for"
				},
				"shouldEndSession": True
			  }
			}


def lambda_handler(event, context):
	deviceID = event["context"]["System"]['device']['deviceId']
	key = event["context"]["System"]['apiAccessToken']

	return createResponse(place)

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


#vincenty((34.7189472, -82.3064414), (34.6708859002, -82.8352496018))
