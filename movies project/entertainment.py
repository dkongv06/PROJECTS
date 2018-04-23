#this file is to learn how to use the class Movie we created to work with this

import database
import fresh_tomatoes

toy_story = database.Movie("Toy Story", "A story of a boy and his toys that come to life.", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#toy_story is an instance of the class Movie that we created in database.py, this is a term called instance variable
#first thing that happens when ^^^^^code is run is a init() funcion
#toy_story = self, self is from database.py aka the instance being created
print(toy_story.storyline)

avatar = database.Movie("Avatar", "A marine on an alien planet.", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
print (avatar.storyline)
###avatar.show_trailer()
#if you remove #'s from above line you have a code that will access a function called show_trailer() within the instance avatar.XXX from the file databse.py that we created separately

inception = database.Movie("Inception", "Thieves infiltrate people's dreams to steal information.", "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg", "https://www.youtube.com/watch?v=YoHD9XEInc0")
print (inception.storyline)

jumanji = database.Movie("Jumanji", "Kids discover a new world by playing this board game.", "https://upload.wikimedia.org/wikipedia/en/b/b6/Jumanji_poster.jpg", "https://www.youtube.com/watch?v=DvQ-PGUr6SM")
print (jumanji.storyline)

movies = [toy_story, avatar, inception, jumanji]
#this is an array of all the movies we created, moives is made to create a list of movies we want in our website

fresh_tomatoes.open_movies_page(movies)

print(database.Movie.VALID_RATINGS)
