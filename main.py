import sys
import json
import webbrowser
from news import News
from prefManager import PrefManager
from help_command import Help_Command

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
					url = news.getStoryURL(sourceName, story_number)
					if(not url is None):
						webbrowser.open(url)
					else:
						print("Could not find a URL for that story.")
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
		elif(commandArray[0] == "remove"):
			if(len(commandArray) > 1):
				prefManager.remove_source(" ".join(commandArray[1:]))
			else:
				print("Too few arguments. Please use the format: " +
				      "remove source")
		elif(commandArray[0] == "sps"):
			if(len(commandArray) > 1 and len(commandArray) < 3):
				try:
					prefManager.set_stories_per_source(int(commandArray[1]))
				except ValueError:
					print("Error: Invalid number of stories. Please enter an integer greater than 0.")
			else:
				print("Invalid command. Please use the format sps storyNumber")
		elif(commandArray[0] == "random"):
			news.random_story()
		elif(commandArray[0] == "refresh"):
			#Can repost stories without calling API again by passing -local switch.
			news.refresh(commandArray)
		elif(commandArray[0] == "help"):
			Help_Command.help_handler(commandArray)
			#Refactor news stories into own model, and have news_manager
			#Refactor code from command handler to specific command handlers.
			#Refactor API key into raab_requests
			#Implement help method.
			#Generate preferences file if one is not found. Stops you propogating news sources via preferences to others.
			#Write batch file to fire on startup, close after x time.
		elif(commandArray[0] == "exit"):
			sys.exit()
		else:
			print("Unknown command")
			commandHandler()
	else:
		print("Unknown command")
	commandHandler()

prefManager = PrefManager()
print("Welcome to the news! Thanks to newsapi.org for their lovely API!")
print("Please use the 'help' command for a full list and explanation of all commands!")
print("Loading news...")	
news = News(prefManager)
commandHandler()