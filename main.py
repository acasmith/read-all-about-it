import sys
import json
import webbrowser
import news as nw
from prefManager import PrefManager

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
			#refactor request making code into own utility class.
		elif(commandArray[0] == "remove"):
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

prefManager = PrefManager()
print("Welcome to the news! Thanks to newsapi.org for their lovely API!")
print("Loading news...")	
news = nw.News(prefManager)
commandHandler()