import sys
import json
from utils.menu import Menu
from core.prefs import Preferences
from utils.raab_requests import Raab_Requests

class PrefManager:
    
    def __init__(self):
        try:
            with open("prefs.json", "r") as read_file:
                self.prefs = Preferences(json.load(read_file))
        except FileNotFoundError:
            self.exit_handler("No preferences file found. " +
                    "Please create a new file names prefs.json in your " +
                    "read-all-about-it directory and copy over the example " +
                    "found in example-prefs.json, replacing the example api" +
                    "key with your own.")
        except json.decoder.JSONDecodeError:
            PrefManager.exit_handler("The file prefs.json could not be parsed " +
                    "as json. Please copy the example found in example-prefs.json and " +
                    "paste it into prefs.json, replacing the example api key " +
                    "with your own.")
    
    #Don't like having an exit here, find a way to move it into main so entry and exit same place.
    def exit_handler(message):
        print(message)
        sys.exit()
            
    def get_prefs(self):
        return self.prefs
    
    def get_sources(self):
        return self.prefs.get_sources()
    
    def get_api_key(self):
        return self.prefs.get_api_key()
    
    def get_stories_per_source(self):
        return self.prefs.get_stories_per_source()
    
    def addSource(self, source_name):
        params = {'apiKey': self.prefs.get_api_key()}
        source_list = Raab_Requests.make_request("top_sources", params)
        if source_list is None: return
        match = self.find_source(source_list['sources'], source_name)
        if match != -1 and match != -2:
            confirm_statement = "Add " + match['name'] + " to followed sources?"
            if Menu.confirm_change(confirm_statement):
                self.prefs.add_source({'name': match['name'], 'id': match['id'], 'description': match['description']})
                if(self.save_changes()):
                    print("Now following " + match['name'] + ".")
            else:
                print("Cancelled. Preferences not changed.")
        
    def remove_source(self, source_name):
        match = self.find_source(self.prefs.get_sources(), source_name)
        if match != -1 and match != -2:
            confirm_statement = "Remove " + match['name'] + " from followed sources?"
            if(Menu.confirm_change(confirm_statement) and
                                   self.prefs.remove_source(match) and
                                   self.save_changes()):
                print("No longer following " + match['name'] + ".")
            else:
                print("Cancelled. Preferences not changed.")
                        
    def save_changes(self):
        try:
            with open("prefs.json", "w") as write_file:
                json.dump(self.prefs.get_prefs(), write_file)
            return True
        except Exception as e:  #Find more specific exception(s) to target
            print("Could not save preferences changes. Please check prefs.json exists and matches the format of expamle-prefs.json.")
            print(e)
            return False
                
    def find_source(self, source_list, source_name):
        matches = []
        for source in source_list:
            if(source_name in source['name']):
                matches.append(source)
        if len(matches) > 0:
            match = matches[0]
            if len(matches) > 1:
                match = Menu.numeric_menuf(Menu, matches, self.format_source)
        else:
            match = -2
        if match == -1:
            print("Cancelled. Preferences not changed.")
        elif match == -2:
            print("No matching source found for \"" + source_name + "\"")
        return match
            
    def get_top_sources(self):
        params = {'apiKey': self.prefs.get_api_key()}
        return RaabRequests.make_request("top_sources", params)
    
    def format_source(self, source):
        formattedSource = source['name'] + ": "
        formattedSource += source['description'] + "\n"
        return formattedSource
    
    def set_stories_per_source(self, nos):
        if(not(nos is None) and
           (type(nos) is int) and
           (nos > 0)):
            self.prefs.set_stories_per_source(nos);
            self.save_changes();
        else:
            print("Invalid parameter. Please enter an integer greater than 0.")