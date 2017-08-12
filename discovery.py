

#discovery = watson_developer_cloud.DiscoveryV1(
#                version='2016-11-07',
#				username='35271d59-360e-45f5-90e6-4c85e5687a7c',
#               password='s0EiiKmlkxWe')

##old one               
#discovery = watson_developer_cloud.DiscoveryV1(
#username='35271d59-360e-45f5-90e6-4c85e5687a7c',
#password='s0EiiKmlkxWe',
#version='2017-08-01')
## new one
def discoveryData(text):
	import json
	import watson_developer_cloud
	import csv
	import sys
	import pandas as pd
	discovery1 = watson_developer_cloud.DiscoveryV1(
	username='438ed2d6-4d74-45f4-87b4-15f2d0af0d59',
	password='jnpKtiO52kmp',
	version='2017-08-01')
	#discovery = DiscoveryV1(
	#  username="{username}",
	#  password="{password}",
	#  version="2017-08-01"
	#)
	
	environments = discovery1.get_environments()
	#print environments
	#news_environments = [x for x in environments['environments'] if x['name'] == 'Watson News Environment']
	#Watson System Environment
	news_environments = [x for x in environments['environments'] if x['name'] == 'Watson System Environment']
	#print news_environments
	news_environment_id = news_environments[0]['environment_id']
	
	collections = discovery1.list_collections(news_environment_id)
	#print ">>>>>>>>>>>>>>>>>>>>>>>>>"
	#print collections
	#news_collections = [x for x in collections['collections']]
	#news_collections = [x for x in collections['collections']if x['name'] == 'Watson System Environment']]
	news_collections_id= collections['collections'][0]['collection_id']
	#print news_collections_id
	#configurations = discovery.list_configurations(
	#               environment_id=news_environment_id)
	#default_config_id = discovery.get_default_configuration_id(
	#                environment_id=news_environment_id)
	
	#default_config = discovery.get_configuration(
	#               environment_id=news_environment_id, configuration_id=default_config_id)
	
	#"count":1,
	query_options = {"count":50,
	"return": "title,url",
	#  enriched_text.concept
	"query":text
	# "aggregations": "filter(relations.location.entities.type::Country)"
	#  "filter": "blekko.hostrank>20,blekko.chrondate>1486146600,blekko.chrondate<149x44200"
	#}
	# "filter" : "(enriched_title.keywords.text::cell theory)"
	}
	query_results = discovery1.query(news_environment_id,news_collections_id,query_options)
	#print news_environment_id
	#print news_collections[0]['collection_id']                                                                                                                            
	query_json= (json.dumps(query_results, indent=2))                                
	query_json1 = json.loads(query_json)   
	#print query_results["results"][0]["score"]
	score = []
	for i in range(0,len(query_results["results"])):
		score.append(query_results["results"][i]["score"])
	
	answers = []
 
	for i in range(0,len(query_results["results"])):
		if query_results["results"][i]["score"] == max(score):
			answers.append(query_results["results"][i]["title"])
			answers.append(query_results["results"][i]["url"])
	
	return (answers)

  
