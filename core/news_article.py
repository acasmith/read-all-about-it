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