import json

val = """{
  "languageModel": {
	"types": [
	  {
		"name": "wordList",
		"values": [
		"""
values = []
with open('result.json') as json_data:
	d = json.load(json_data)
for k, v in d.items():
	for k1, v1 in v.items():
		if k1 not in values:
			values.append(k1)
completed = []
for v in list(set(values)):
	valAdd = """{
            "id": null,
            "name": {
              "value": "word1",
              "synonyms": []
            }
          },""".replace('word1', v.lower())
	if str(valAdd) not in completed:
		val = val + valAdd
    	completed.append(valAdd)

val = val + """ ]
      }
    ],
    "intents": [
      {
        "name": "AMAZON.CancelIntent",
        "samples": []
      },
      {
        "name": "AMAZON.HelpIntent",
        "samples": []
      },
      {
        "name": "AMAZON.StopIntent",
        "samples": []
      },
      {
        "name": "startDiagnosis",
        "samples": [
          "start diagnosis",
          "diagnose me",
          "speech diagnose",
          "speech diagnosis",
          "speech test",
          "test my speech",
          "test my speech abilities",
          "how well do i speak",
          "start a diagnostic test"
        ],
        "slots": []
      }
    ],
    "invocationName": "daa"
  }
}"""
file = open("testfile.txt", "w")
file.write(val)
