import sys
import json
import news as nw

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
				      "expand source_name story_number")
		elif(commandArray[0] == "browser"):
			print("browser branch called")
		elif(commandArray[0] == "add"):
			print("add branch called")
		elif(commandArray[0] == "nos"):
			print("nos branch called")
		elif(commandArray[0] == "random"):
			print("random headline branch called")
		elif(commandArray[0] == "refresh"):
			print("refreshing stories")
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