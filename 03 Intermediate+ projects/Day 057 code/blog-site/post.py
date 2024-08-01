class Post:
    def __init__(self, dict):
        self.title = dict["title"]
        self.subtitle = dict["subtitle"]
        self.body = dict["body"]
        self.id = dict["id"]
    
    def get_title(self):
        return self.title
    
    def get_subtitle(self):
        return self.subtitle
    
    def get_body(self):
        return self.body
    
    def get_id(self):
        return self.id