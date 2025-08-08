import kagglehub

path = kagglehub.dataset_download("prajitdatta/movielens-100k-dataset")
print("Path to dataset files:", path)
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