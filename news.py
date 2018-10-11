from raab_requests import Raab_Requests
class News:
    
    def __init__(self, pref_manager):
        self.stories = {}
        self.pref_manager = pref_manager
        self.getStories()
        self.showNews()
                
    def getStories(self):
        sources = self.pref_manager.get_sources()
        params = {'apiKey': self.pref_manager.get_api_key()}
        for source in sources:
            params['sources'] = source['id']
            response = Raab_Requests.make_request("top_headlines", params)
            self.stories[source['name']] = response
    
    def showNews(self):
        sources = self.pref_manager.get_sources()
        for source in sources:
            if(self.stories[source['name']]["status"] == "ok"):
                print(self.sourceSummary(source['name'], self.pref_manager.get_stories_per_source()))
            else:
                print(self.formatRequestError(source))
            

    def sourceSummary(self, source_name, stories_per_source):
        summaryString = source_name + " Headlines: \n"
        for x in range(0, stories_per_source):
                summaryString += self.formatArticle(self.stories[source_name]["articles"][x], x + 1) + "\n"
        return summaryString
    
    def formatRequestError(self, source_name):
        message = "************Request Error***********\n"
        message += "News source: " + source_name + "\n"
        message += "Request status: " + self.stories[source_name]["status"] + "\n"
        message += "Request status code: " + self.stories[source_name]["code"] + "\n"
        message += "Message: " + self.stories[source_name]["message"]
        return message
    
    def formatArticle(self, article, articleNumber):
        formattedString = str(articleNumber) + ") "
        formattedString += article['title']
        return formattedString
    
    def previewStory(self, source_name, story_number):
        storyPreview = ""
        if source_name in self.stories.keys():
            if(story_number >= 0 and story_number < len(self.stories[source_name])):
                article = self.stories[source_name]['articles'][story_number]
                storyPreview = article['title'] + "\n"
                storyPreview += article['description'] + "\n"
                storyPreview += article['content']
            else:
                storyPreview = "Source has no corresponding story for that article number."
        else:
            storyPreview = ("No stories loaded for that source. If it is a new " +
                            "source please use the add command to add the source " +
                            "to your news feed.")
        print(storyPreview)
        
    def getStoryURL(self, source, story_number):
        return self.stories[source]['articles'][story_number]['url']
    
    def refresh(self, commandArray):
        if(len(commandArray) == 1 or
           commandArray[1] != '-local'):
            self.getStories()
        self.showNews()
    #random story