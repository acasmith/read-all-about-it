import requests
import json

class PrefManager():
    base_url = "https://newsapi.org/v2/"
    top_sources = base_url + "sources"
    prefs = None
    
    def __init__(self):
        try:
            with open("prefs.json", "r") as read_file:
                self.prefs = json.load(read_file)
        except FileNotFoundError:
            print("No preferences file found. Would you like to generate a new one? (y/n)")
            self.generate_prefs()
        except json.decoder.JSONDecodeError:
            print("prefs.json could not be parsed as json. Generate a new preferences file? (y/n:)")
            self.generate_prefs()
            
            #generate new prefs file. Put y/n in generate function to cap input.
    
    def addSource(self, source_name):
        source_list = self.get_top_sources()
        match = self.find_source(source_list, source_name)
        if match != -1 and match != -2:
            confirm_statement = "Add " + match['name'] + " to followed sources?"
            if self.confirm_source_change(confirm_statement):
                self.prefs['sources'].append({'name': match['name'], 'id': match['id'], 'description': match['description']})
                if(self.save_changes()):
                    print("Now following " + match['name'] + ".")
            else:
                print("Cancelled. Preferences not changed.")
            
            #0 matches = offer manual addition
            #1 match = confirm
            #>1 matches = offer selection then confirm.
            
        #pull down sources
        #filter sources for name
        #if found, add to prefs
        #else offer to take to page to get source and add it manually.
        
    def remove_source(self, source_name):
        match = self.find_source(self.prefs, source_name)
        if match != -1 and match != -2:
            confirm_statement = "Remove " + match['name'] + " from followed sources?"
            if self.confirm_source_change(confirm_statement):
                for i in range(0, len(self.prefs['sources'])):
                    if self.prefs['sources'][i] == match:
                        del self.prefs['sources'][i]
                        if(self.save_changes()):
                            print("No longer following " + match['name'] + ".")
                        
                        
    def save_changes(self):
        try:
            with open("prefs.json", "w") as write_file:
                json.dump(self.prefs, write_file)
            return True
        except Exception as e:
            print("Could not save preferences changes. Please check prefs.json exists and matches the format of expamle-prefs.json.")
            return False
                
    def find_source(self, source_list, source_name):
        matches = []
        for source in source_list['sources']:
            if source_name in source['name']:
                matches.append(source)
        if len(matches) > 0:
            match = matches[0]
            if len(matches) > 1:
                match = self.choose_source(matches)
        else:
            match = -2
        if match == -1:
            print("Cancelled. Preferences not changed.")
        if match == -2:
            print("No matching source found for \"" + source_name + "\"")
        return match
                
        
        
        
    def get_top_sources(self):
        params = {
            'apiKey': self.prefs['api-key']
        }
        try:
            print("Searching for sources...")
            response = requests.get(self.top_sources, params)
            response = response.json()
            return response
        except requests.exceptions.RequestException as e:
            print(e)
        except ValueError as e: #Could not parse response as JSON
            print(e)
     
    #offer each option as a numbered menu       
    def choose_source(self, menu_items):
        for x in range(0, len(menu_items)):
            print(str(x + 1) + ") " + self.format_source(menu_items[x]))
        print("Please enter the number you wish to choose, or enter exit to cancel:")
        return self.parse_menu_input(menu_items);
    
    #Split from menu choice in case other forms of parsing required,
    #which could then be passed as an arg to choose_source ie. this would be numeric,
    #another could be string etc.
    def parse_menu_input(self, menu_items):
        response = input(">>>")
        if response == "exit":
            return -1
        try:
            response = int(response)
            if (response > 0 and response <= len(menu_items)):
                return menu_items[response - 1]
        except ValueError:
            pass
        print("Please enter a valid number, or type exit to cancel.")
        return self.parse_menu_input(menu_items)
    
    def format_source(self, source):
        formattedSource = source['name'] + ": "
        formattedSource += source['description'] + "\n"
        return formattedSource
        
    
    def confirm_source_change(self, confirm_statement):
        print(confirm_statement + " (y/n):")
        response = input(">>>")
        if(response == "y" or response == "yes" or response == "YES"):
            return True
        elif(response == "n" or response == "no" or response == "NO"):
            return False
        print("Invalid input.")
        return self.confirm_source_addition(match)
        
    
    def generate_prefs(self):
        pass