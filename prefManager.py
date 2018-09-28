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
        except JSONDecodeError:
            print("prefs.json could not be parsed as json. Generate a new preferences file? (y/n:)")
            self.generate_prefs()
            
            #generate new prefs file. Put y/n in generate function to cap input.
    
    def addSource(self, source_name):
        source_list = self.get_top_sources()
        matches = []
        for source in source_list['sources']:
            if source_name in (source['name']):
                matches.append(source)
        if len(matches) > 0:
            match = matches[0]
            if len(matches) > 1:
                print("Multiple options found for \"" + source_name + "\":")
                match = self.choose_source(matches)
            if(match != -1 and self.confirm_source_addition(match)):
                self.prefs['sources'][match['name']] = match['id']
                try:
                    with open("prefs.json", "w") as write_file:
                        json.dump(self.prefs, write_file)
                    print("Source added to preferences")
                except Exception as e:
                    print("Could not save new source. Please check prefs.json exists and matches the format of expamle-prefs.json.")
            else:
                print("Cancelled. No source added.")
        else:
            print("No matching source found for \"" + source_name + "\"")
            
            #0 matches = offer manual addition
            #1 match = confirm
            #>1 matches = offer selection then confirm.
            
        #pull down sources
        #filter sources for name
        #if found, add to prefs
        #else offer to take to page to get source and add it manually.
        
    '''def remove_source(self, source_name):
        matches = []
        for source in source_list['sources']:
            if source_name in (source['name']):
                matches.append(source)
        if len(matches) > 0:
            match = matches[0]
            if len(matches) > 1:
                match = self.choose_source(matches)'''
                
    def edit_sources(self, source_list):
        matches = []
        for source in source_list['sources']:
            if source_name in (source['name']):
                matches.append(source)
        if len(matches) > 0:
            match = matches[0]
            if len(matches) > 1:
                match = self.choose_source(matches)
            return match
        return -2
                
        
        
        
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
        
    
    def confirm_source_addition(self, match):
        print("Add " + match['name'] + " to followed sources? (y/n):")
        response = input(">>>")
        if(response == "y" or response == "yes" or response == "YES"):
            return True
        elif(response == "n" or response == "no" or response == "NO"):
            return False
        print("Invalid input.")
        return self.confirm_source_addition(match)
        
    
    def generate_prefs(self):
        pass