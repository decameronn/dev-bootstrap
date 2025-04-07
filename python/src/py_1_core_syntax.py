
# Core Syntax & Data Types
# ********************************************************
# integer
a = 10
# float
b = 10.5
# string
word = "Hello, World!"
# boolean
is_great = True

# list ( ordered mutable collection )
fruits = ["apple", "banana", "cherry"]

# tuple ( ordered immutable collection )
base_location = (43.12, 76.34)

# set ( unordered collection of unique elements )
odd_numbers = {1, 3, 5, 7, 9}

# dictionary ( key-value pairs )
person = {
    "name": "John Doe",
    "age": 30,
    "is_student": False
}

# None ( represents the absence of a value )
nothing = None


# Practice
# ********************************************************

# 1. Create a list of three of your favorite movies.
fav_movies = ["inception", "matrix", "stalker"]

# 2. Create a dictionary to store your favorite movie along with its release year.
fav_movie = { "inception": 2010 }

# 3. Create a tuple for the coordinates of your favorite place.
fav_place  = (40.7128, 74.0060) 

# 4. Description should be deduced from the code
# list of movies (tuples)
list_of_movies = [
    ("interstellar", 2014, "sci-fi"),
    ("matrix", 1999, "sci-fi"),
    ("stalker", 1979, "drama"),
    # adding a new movie
    ("pandorum", 2009, "sci-fi") 
]

movie_rating = {
    "interstellar": 8.7,
    "matrix": 8.7,
    "stalker": 8.0,
    # a new movie
    "pandorum": 6.7
}

# 5. Access the 2nd movie from list_of_movies
second_movie = list_of_movies[1]
print(second_movie)

# 6. Access the rating of "stalker" from movie_rating
rating_stalker = movie_rating["matrix"]
print(rating_stalker)

# 7. Update the rating of a movie
movie_rating["pandorum"] = 8.3
