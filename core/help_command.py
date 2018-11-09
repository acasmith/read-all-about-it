#Model for descriptions of each of raab's commands. This class is not used anywhere except in Help_Command.
class Command_Description:
    
    def __init__(self, name, description, command_format, examples):
        self.name = name
        self.description = description
        self.command_format = command_format
        self.examples = examples
        
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
    
    def get_command_format(self):
        return command_format
    
    def examples(self):
        return examples
    
    def to_string(self):
        string = "Command: " + self.name + "\n"
        string += "Description: " + self.description + "\n"
        string += "Format: " + self.command_format + "\n"
        string += "Examples: " + self.examples
        return string

#Contains explanations of all commands for the Read All About It news aggregator.
class Help_Command:
    @staticmethod
    def general_help():
        description = '''
General Help:
Enter 'help someCommandName' to get a full description of a particular command. Eg. help preview \n
Commands:
preview: Displays a short preview of a particular story.
open: Opens a particular story in the systems default web browser.
add: adds a news source to the users preferences so news from this agency is displayed on startup.
remove: removes a news source from the users preferences.
sps: Standing for 'stories per source', allows the user to specify the number of headlines to
display per news source.
random: Fetches a random headline from a random news source.
refresh: displays current headlines 
'''
        return description
    
    commands = {
        "preview": Command_Description("preview",
                                     "Displays a short preview of a particular story. " +
                                        "Requires the news source name and headline story number.",
                                    "preview newsSource storyNumber",
                                    "preview BBC News 2"),
        "open": Command_Description("open",
                                    "Opens a particular story in the systems default web browser." +
                                        "Requires the news source name and headline story number.",
                                    "open newsSource storyNumber",
                                    "open BBC Sport 3"),
        "add": Command_Description("add",
                                   "Adds a news source to the users preferences so news from this agency is displayed on startup. " +
                                   "Close matches will be offered if there is no exact match for the specified source.",
                                   "add newsSource",
                                   "add BBC"),
        "remove": Command_Description("remove",
                                      "Removes a news source from the users preferences so it is no longer displayed on startup." +
                                        "Close matches will be offered if there is no exact match for the specified source.",
                                      "remove newsSource",
                                      "remove BBC"),
        "sps": Command_Description("sps",
                                   "Standing for 'stories per source', allows the user to specify the number of headlines to " +
                                    "display per favourited news source.",
                                    "sps numberOfStories",
                                    "sps 4"),
        "random": Command_Description("random",
                                      "Fetches and displays a random headline from a random news source.",
                                      "random",
                                      "random"),
        "refresh": Command_Description("refresh",
                                       "Fetches and displays current headlines from favourited news sources. " +
                                       "Can provide an optional -local switch to prevent fetching of stories " +
                                       "from the network and only display cached headlines from the last retrieval.",
                                       "refresh",
                                       "refresh \nrefresh -local")
    }
    
    @staticmethod
    def help_handler(commandArray):
        result = None
        command = commandArray[0]
        if len(commandArray) == 1:
            result = Help_Command.general_help()
        else:
            command = commandArray[1]
            for key in Help_Command.commands.keys():
                if command == key:
                    result = Help_Command.commands[key].to_string()
        if result is None:
            result = "Could not find a description of that command."
        print(result)
    
    
    '''
    preview
    open
    add
    remove
    sps
    random
    refresh
    '''
    
    '''
    each command has a:
    name
    description
    format
    examples
    '''