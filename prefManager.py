import requests
import json

class PrefManager():
    base_url = "https://newsapi.org/v2/"
    top_sources = base_url + "sources"
    prefs = None
    
    def __init__(self):
        with open("prefs.json", "r") as read_file:
            self.prefs = json.load(read_file)
    
    def addSource(self, sourceName):
        source_list = self.get_top_sources()
        matches = []
        for source in source_list['sources']:
            if sourceName in (source['name']):
                matches.append(source)
        if len(matches) > 0:
            if len(matches) > 1:
                match = self.chooseSource(matches)
                pass
            else:
                match = matches[0]
            user_input = input(">>>Add " + match['name'] + " to favourites? (y/n): ")
            if(self.validateInput(user_input)):
                #add to prefs
                pass
            else:
                print("Cancelled. No source added.")
                
            
        else:
            print("No matching source found.")
            
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
            
    def chooseSource(self, matches):
        pass
    
    def validateInput(self, user_input):
        pass