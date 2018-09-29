import sys
import json
import webbrowser
import news as nw
import prefManager as pm

#In hindsight, should've made a class for prefs so rest of program could easier manage
#any underlying changes 
def commandHandler():
	command = input(">>>")
	if(command != None and len(command) > 0):
		commandArray = command.split(" ")
		if(commandArray[0] == "preview"):
			if(len(commandArray) >= 3):
				try:
					story_number = int(commandArray[len(commandArray) - 1]) - 1
					sourceName = " ".join(commandArray[1:len(commandArray)-1])
					news.previewStory(sourceName, story_number)
				except ValueError:
					print("Error: invalid article number.")
			else:
				print("Too few arguments. Please use the format: " +
				      "preview source_name story_number")
		elif(commandArray[0] == "open"):
			if(len(commandArray) >= 3):
				try:
					story_number = int(commandArray[len(commandArray) - 1]) - 1
					sourceName = " ".join(commandArray[1:len(commandArray)-1])
					webbrowser.open(news.getStoryURL(sourceName, story_number))
				except ValueError:
					print("Error: invalid article number.")
			else:
				print("Too few arguments. Please use the format: " +
				      "open source_name story_number")
		elif(commandArray[0] == "add"):
			if(len(commandArray) > 1):
				prefManager.addSource(" ".join(commandArray[1:]))
			else:
				print("Too few arguments. Please use the format: " +
				      "add source")
			#add get prefManager to deal with prefs, pull out of main.
			#refactor request making code into own utility class.
			#refactor menu offering code into utility class.
		elif(commandArray[0] == "remove"):
			print("remove branch called")
			if(len(commandArray) > 1):
				prefManager.remove_source(" ".join(commandArray[1:]))
			else:
				print("Too few arguments. Please use the format: " +
				      "remove source")
		elif(commandArray[0] == "nos"):
			print("nos branch called")
		elif(commandArray[0] == "random"):
			print("random headline branch called")
		elif(commandArray[0] == "refresh"):
			print("refreshing stories")
			#have option to just repost stories without calling API again.
		elif(commandArray[0] == "help"):
			print("help branch called")
		elif(commandArray[0] == "exit"):
			sys.exit()
		else:
			print("Unknown command")
			commandHandler()
	else:
		print("Unknown command")
	commandHandler()
		
	#expand story: expand source storyNumber
	#open story in browser: browser source storyNumber -w -t
	#add source: add source sourceName
	#number of stories: nos someInt
	#random headline: random
prefManager = pm.PrefManager()
with open("prefs.json", "r") as read_file:
	prefs = json.load(read_file)
print("Welcome to the news! Thanks to newsapi.org for their lovely API!")
print("Loading news...")	
news = nw.News(prefs)
commandHandler()

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