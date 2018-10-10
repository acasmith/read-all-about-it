class Preferences:
    def __init__(self, prefs):
        self.prefs = prefs

    def get_prefs(self):
        return self.prefs
        
    def get_sources(self):
        return self.prefs['sources']
    
    def get_api_key(self):
        return self.prefs['api-key']
    
    def get_stories_per_source(self):
        return self.prefs['stories-per-source']
    
    def add_source(self, source):
        self.prefs['sources'].append(source)
        
    def remove_source(self, source):
        sources = self.get_sources()
        for i in range(0, len(sources)):
                    if sources[i] == source:
                        del self.prefs['sources'][i]
                        return True
        return False
    
    def set_stories_per_source(self, nos):
        self.prefs['stories-per-source'] = nos
        print(self.get_prefs()['stories-per-source'])
            
    
    