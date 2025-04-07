# Control Flow

# if, elif, else
x = 10
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

# for loop
for i in range(10):
    print("Count is:", i)
    i += 2

# while loop
i = 0
while i < 4:
    print("Count is:", i)
    i += 1


# Practice
# ********************************************************

# 1. Check if Pandorum rating is greater than 7.0.
#    If yes, print "Great movie!", otherwise print "Not so great."
movie_ratings = {
    "interstellar": 8.7,
    "matrix": 8.7,
    "stalker": 8.0,
    "pandorum": 6.7
}
for movie in movie_ratings:
    if movie_ratings["pandorum"] >= 7.0:
        print("Great movie!")
    else:
        print("Not so great.")

# 2. Loop through list_of_movies and print each title
#    with the text " is in your collection!"
list_of_movies = [
    ("interstellar", 2014, "sci-fi"),
    ("matrix", 1999, "sci-fi"),
    ("stalker", 1979, "drama"),
    ("pandorum", 2009, "sci-fi") 
]
for m in list_of_movies:
    print(m[0], "is in your collection!")

