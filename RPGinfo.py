class RPGinfo():
    author = 'Anonymous'

    def __init__(self,game_title):
        self.title = game_title

    def welcome(self):
        print('welcome to '+ self.title)

    # example of a static method:
    def info():
        print('Made using the OOP programing method')

    # example of a class method:
    def credits(cls):
        print('Thank you for playing\nCreated by ' + cls.author)
