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
            print("No preferences file found. Would you like to generate a new one?")
            self.generate_prefs()
            #generate new prefs file
    
    def addSource(self, source_name):
        source_list = self.get_top_sources()
        matches = []
        for source in source_list['sources']:
            if source_name in (source['name']):
                matches.append(source)
        if len(matches) > 0:
            match = matches[0]
            if len(matches) > 1:
                match = self.choose_source(matches, source_name)
            if(match != -1 and self.confirm_source_addition(match)):
                print("Source added to prefs")
                #add to prefs
                pass
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
        
    def get_top_sources(self):
        params = {
            'apiKey': self.prefs['api-key']
        }
        try:
            response = requests.get(self.top_sources, params)
            response = response.json()
            return response
        except requests.exceptions.RequestException as e:
            print(e)
        except ValueError as e: #Could not parse response as JSON
            print(e)
     
    #offer each option as a numbered menu       
    def choose_source(self, matches, source_name):
        print("Multiple options found for \"" + source_name + "\":")
        for x in range(0, len(matches)):
            print(str(x + 1) + ") " + self.format_source(matches[x]))
        print("Please enter the number of the source you wish to add, or enter exit to cancel:")
        return self.parse_menu_input(matches);
        
    def parse_menu_input(self, matches):
        response = input(">>>")
        if response == "exit":
            print("exit branch called")
            return -1
        try:
            response = int(response)
            if (response > 0 and response <= len(matches)):
                return matches[response - 1]
        except ValueError:
            pass
        print("Please enter a valid number, or type exit to cancel.")
        return self.parse_menu_input(matches)
    
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