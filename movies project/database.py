#this project is learning how to create our own class called "Movie" for a program that contatins a database of movies
#other classes we have used are Turtle but we want to create a new one now
#we want this database to show a title, trailer, poster, story line
import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
    #__doc__ is a preexisting class varibale that will access ^^^above info within """XXX"""
    #python has more predefined class variables like "__name__" and "__module__"

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    #use all caps if what is in the array is constant or will not change, lower case if they are subject to changef

#self.storyline = XXX is a instance variable accessible within instance toy_story.XXX or avatar.XXX, remove "self" and storyline = XXX is a local varibale inside the fucntion init()

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    #this function we have defined is an instance method
