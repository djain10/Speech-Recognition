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

def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

def valToNum(wordVal):
  word = wordVal.replace("word", "").lower().replace("thirty", "thirty ").replace("twenty", "twenty ")
  return text2int(word)

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

def getAllSlots(intent):
	dictValue = {}
	sentence = ""
	for slot in intent['intent']['slots'].keys():
		try:
			numVal = str(valToNum(intent['intent']['slots'][slot]['name']))
			dictValue[numVal] = intent['intent']['slots'][slot]['value']
		except Exception as exp:
			pass
	i = 0
	for i in range(1,40):
		try:
			sentence = sentence + " " + dictValue[str(i)]
		except:
			pass
	return sentence

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
		print getAllSlots(intent_request)
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
