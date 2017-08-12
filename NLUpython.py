def NLUData(question):
	import json
	from watson_developer_cloud import NaturalLanguageUnderstandingV1
	import watson_developer_cloud.natural_language_understanding.features.v1 \
	as Features
	
	natural_language_understanding = NaturalLanguageUnderstandingV1(
	username="bf7a6b28-a7cb-4b07-9ca3-d0303f4ebc35",
	password="CiHHmEuXCRh5",
	version="2017-02-27")
	
	response = natural_language_understanding.analyze(
	text=question,
	features=[
		Features.Keywords()
	]
	)
	
	#print(json.dumps(response, indent=2))
	
	relevance = []
	#response["keywords"][0]["relevance"]
	
	for i in range(0,len(response["keywords"])):
		relevance.append(response["keywords"][i]["relevance"])
	
	answer = []
	for i in range(0,len(response["keywords"])):
		if response["keywords"][i]["relevance"] == max(relevance):
			#relevance.append(response["keywords"][i]["relevance"])
			answer.append(response["keywords"][i]["text"])
	
	# var natural_language_understanding = new NaturalLanguageUnderstandingV1({
	# 'username': 'bf7a6b28-a7cb-4b07-9ca3-d0303f4ebc35',
	# 'password': 'CiHHmEuXCRh5',
	# 'version_date': '2017-02-27'
	# });
	
	
	# var parameters = {
	# 'text':'Who proposed the cell theory?',
	# 'language':'en',
	
	# 'features': {
		# 'keywords':{}
	# }
	# };
	
	return (answer)