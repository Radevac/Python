class Recipe:
    def __init__(self, title, author, type, description, video_link, ingredients, cuisine):
        self.title = title
        self.author = author
        self.type = type
        self.description = description
        self.video_link = video_link
        self.ingredients = ingredients
        self.cuisine = cuisine

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "type": self.type,
            "description": self.description,
            "video_link": self.video_link,
            "ingredients": self.ingredients,
            "cuisine": self.cuisine
        }
