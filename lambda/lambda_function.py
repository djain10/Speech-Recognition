import json
import alexaHelper
import random
sentences = open("listOfSentences.txt").read().split("\n")
SKILLNAME = "Alexa Speech Diagnostic Tool"
INITIALSPEECH = "Thank you for checking out the alexa speech diagnostic tool.  We can detect early onset childhood speech disorders"
REPEATSPEECH = INITIALSPEECH

def createResponse(text, endSession=True, sessionCount=0):
	return {
			"version": "1.0",
			"sessionAttributes": {'counter': sessionCount},
			"response": {
			"outputSpeech": {
			"type": "PlainText",
			"text": text
				},
				"shouldEndSession": endSession
			  }
			}


def lambda_handler(event, context):
	print event
	if event["request"]["type"] == "LaunchRequest":
		return alexaHelper.get_welcome_response(SKILLNAME, INITIALSPEECH, REPEATSPEECH)
	elif event["request"]["type"] == "IntentRequest":
		return on_intent(event["request"], event["session"])

def counter_intent(event, context):
    session_attributes = event['session']['attributes']
    if "counter" in session_attributes:
        session_attributes['counter'] += 1

    else:
        session_attributes['counter'] = 1

    return conversation("counter_intent",
                        session_attributes['counter'],
                        session_attributes)

def conversation(title, body, session_attributes):
    speechlet = {}
    speechlet['outputSpeech'] = build_PlainSpeech(body)
    speechlet['card'] = build_SimpleCard(title, body)
    speechlet['shouldEndSession'] = False
    return build_response(speechlet,
                          session_attributes=session_attributes)


def on_intent(intent_request, session):
	print str(session)
	intent = intent_request["intent"]
	intent_name = intent_request["intent"]["name"]
	if intent_name == "startDiagnosis":
		return createResponse("Repeat the following sentence. {}".format(random.choice(sentences)), False)
	elif intent_name == "readSentence":
		print session['attributes']['counter']
		e = session['attributes']['counter']
		count = e + 1
		if count > 2:
			return createResponse("End session", True, sessionCount=count)
		else:
			return createResponse("Repeat the following sentence. {}".format(random.choice(sentences)), False, sessionCount=count)

	elif intent_name == 'aboutDev':
		return alexaHelper.devInfo()
	elif intent_name == "AMAZON.HelpIntent":
		return alexaHelper.get_welcome_response()
	elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
		return alexaHelper.handle_session_end_request()
