import os

# database
file = open("data\imdb_top_1000.csv", mode="r")
genres = file['Genre']
rating = file['IMBD_rating']
title = file['Series_Title']
year = file['Release_Year']
length = file['Runtime']
overview = file['Overview']
director = file['Director']
lead = file['Star1']
class MovieRecs:
    def __init__(self):
        self.self = self
    def greet():
        print("Hello! I heard you need help picking a movie tonight!")
        print("I'm going to ask you some questions so that we can pick a perfect movie!")
       
    def get_genre():
        user_genre = input("What genre/genres are you in the mood for? ")
        return print(user_genre)

        
    def bye():
        print("Hope you enjoy your movie!\n Remember to log it on LetterBoxed!")
        
    def main():
        MovieRecs.greet()
        MovieRecs.get_genre()
        MovieRecs.bye()
    
MovieRecs.main()