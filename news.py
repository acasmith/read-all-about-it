import requests
class News:
    stories = {}
    base_url = "https://newsapi.org/v2/"
    top_headlines = base_url + "top-headlines"
    
    #Would prefer a callback from getStories, but keeping it simple for now.
    def __init__(self, prefs):
        self.getStories(prefs)
        self.showNews(prefs['sources'], prefs['stories-per-source'])
        
    def getStories(self, prefs):
        sources = prefs['sources']
        for source in sources:
            sourceID = sources[source]
            params = {
                    'sources': sourceID,
                    'apiKey': prefs['api-key']
            }
            response = requests.get(self.top_headlines, params=params)
            try:
                self.stories[source] = response.json()
            except Exception as e:
                print("*******************" +
                      "Error converting response to JSON" +
                      "******************")
                print(e)
                print("Raw response: \n" + response.text)
    
    def showNews(self, sources, stories_per_source):
        for source in sources:
            if(self.stories[source]["status"] == "ok"):
                print(self.sourceSummary(source, stories_per_source))
            else:
                print(self.formatRequestError(source))
            

    def sourceSummary(self, source, stories_per_source):
        summaryString = source + " Headlines: \n"
        for x in range(0, stories_per_source):
                summaryString += self.formatArticle(self.stories[source]["articles"][x], x + 1) + "\n"
        return summaryString
    
    def formatRequestError(self, source):
        message = "************Request Error***********\n"
        message += "News source: " + source + "\n"
        message += "Request status: " + self.stories[source]["status"] + "\n"
        message += "Request status code: " + self.stories[source]["code"] + "\n"
        message += "Message: " + self.stories[source]["message"]
        return message
    
    def formatArticle(self, article, articleNumber):
        formattedString = str(articleNumber) + ") "
        formattedString += article['title']
        return formattedString
    
    def previewStory(self, source, story_number):
        storyPreview = ""
        if source in self.stories.keys():
            if(story_number >= 0 and story_number < len(self.stories[source])):
                article = self.stories[source]['articles'][story_number]
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
    
    #expand story
    #browser story
    #random story