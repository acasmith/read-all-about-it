import json
import requests

with open("prefs.json", "r") as read_file:
	prefs = json.load(read_file)
base_url = "https://newsapi.org/v2/"
top_headlines = base_url + "top-headlines"
print("Welcome to the news! Thanks to newsapi.org for their lovely API!")
print(top_headlines)

def getMainStories(sources, stories_per_source, api_key):
	print("It's working!")
	for source in sources:
		sourceID = sources[source]
		print(sourceID)
		params = {
			'sources': sourceID,
			'apiKey': api_key
		}
		response = requests.get(top_headlines, params=params)
		try:
			response = response.json()
			if(response["status"] == "ok"):
				for x in range(0, stories_per_source):
					print(response["articles"][x])
			else:
				print(formatRequestError(response))
		except:
			print("*******************" +
			      "Error converting response to JSON. Raw response text:" +
			      "******************")
			print(response.text)
			
def formatRequestError(response):
	message = "************Request Error***********\n"
	message += "Status: " + response["status"] + "\n"
	message += "Status code: " + response["code"] + "\n"
	message += "Message: " + response["message"]
	return message

#TODO
def formatArticle(article):
	pass

getMainStories(prefs["sources"], prefs["stories-per-source"], prefs["api-key"])
#problem:
#get x number of top stories for an unkown number of sources
#process
#for each source
###get id and num stories
###use it to make request
###check request response: if good, return formatted response else return error string for this source
#print collection of news stories
 
#get BBC news stories and print to cmd.
#have option to specify news outlet as arg.
#have option to open news stories in browser