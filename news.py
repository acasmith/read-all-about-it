from raab_requests import Raab_Requests
import random

#Class only used by News_Manager, so placed in same file.
class News_Article:
    
    def __init__(self, article):
        self.article = article
    
    #Returns dict with id and name properties    
    def get_source(self):
        return self.article['source']
    
    def get_authour(self):
        return self.article['author']

    def get_title(self):
        return self.article['title']
    
    def get_description(self):
        return self.article['description']
    
    def get_url(self):
        return self.article['url']
    
    #Not used in this program, here for completeness
    def get_urlToImage(self):
        return self.article['urlToImage']
    
    def get_publishedAt(self):
        return self.article['publishedAt']
    
    def get_content(self):
        return self.article['content']  
    

class News_Manager:
    
    def __init__(self, pref_manager):
        self.stories = {}
        self.pref_manager = pref_manager
        self.getStories()
        self.showNews()
                
    def getStories(self):
        sources = self.pref_manager.get_sources()
        params = {'apiKey': self.pref_manager.get_api_key()}    #Refactor API key into raab_requests? Adds additional dependency though.
        for source in sources:
            params['sources'] = source['id']
            response = Raab_Requests.make_request("top_headlines", params)
            self.stories[source['name']] = []
            for article in response['articles']:
                self.stories[source['name']].append(News_Article(article))
    
    def showNews(self):
        sources = self.pref_manager.get_sources()
        for source in sources:
            if (source['name'] in self.stories.keys() and
                len(self.stories[source['name']]) > 0):
                print(self.source_summary(source['name'], self.pref_manager.get_stories_per_source()))
            else:
                print(self.formatRequestError(source))
            

    def source_summary(self, source_name, stories_per_source):
        #Programatically get name from article object, because source_name passed in may be "random".
        summaryString = self.stories[source_name][0].get_source()['name'] + " Headlines: \n"
        for x in range(0, stories_per_source):
                summaryString += self.formatArticle(self.stories[source_name][x], x + 1) + "\n"
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
        formattedString += article.get_title()
        return formattedString
    
    def previewStory(self, source_name, story_number):
        storyPreview = ""
        if source_name in self.stories.keys():
            if(story_number >= 0 and story_number < len(self.stories[source_name])):
                article = self.stories[source_name][story_number]
                storyPreview = article.get_title() + "\n"
                storyPreview += article.get_description() + "\n"
                storyPreview += article.get_content()
            else:
                storyPreview = "Source has no corresponding story for that article number."
        else:
            storyPreview = ("No stories loaded for that source. If it is a new " +
                            "source please use the add command to add the source " +
                            "to your news feed.")
        print(storyPreview)
        
    def getStoryURL(self, source, story_number):
        url = None
        for source_name in self.stories.keys():
            if(source == source_name):
                url = self.stories[source][story_number].get_url()
        if (url is None) and (source == self.stories['random'][0].get_source()['name']):
            url = self.stories['random'][0].get_url()  
        return url
    
    def refresh(self, commandArray):
        print("Refreshing headlines...")
        if(len(commandArray) == 1 or
           commandArray[1] != '-local'):
            self.getStories()
        self.showNews()
    
    #Retrieves and displays a random story from a random news agency to the user.  
    def random_story(self):
        print("Fetching random news story...")
        
        #Grab random source
        params = {'apiKey': self.pref_manager.get_api_key()}
        top_sources = Raab_Requests.make_request("top_sources", params)
        if top_sources is None:
            return
        top_sources = top_sources['sources']
        random_number = random.randint(0, len(top_sources))
        random_source = top_sources[random_number]
        
        #grab random story from source and display
        params['sources'] = random_source['id']
        random_stories = Raab_Requests.make_request("top_headlines", params)
        if random_stories is None:
            return
        self.stories['random'] = []
        for article in random_stories['articles']:
            self.stories['random'].append(News_Article(article))
        print(self.source_summary("random", 1))