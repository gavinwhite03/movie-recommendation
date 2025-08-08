from pathlib import Path
import re
import pandas as pd

class MovieRecs:
    def __init__(self, csv_path="data/imdb_top_1000.csv"):
        self.data = pd.read_csv(Path(csv_path))
        # Clean runtime -> numeric minutes
        if "Runtime" in self.data.columns:
            self.data["Runtime"] = (
                self.data["Runtime"]
                .astype(str)
                .str.replace(" min", "", regex=False)
                .str.extract(r"(\d+)")
                .astype(float)
            )

    def greet(self):
        print("Hello! I heard you need help picking a movie tonight!")
        print("I'm going to ask you some questions so that we can pick a perfect movie!\n")

    def ask_genre(self):
        raw = input("What genre(s) are you in the mood for? (e.g., Action, Drama, Sci-Fi): ")
        return [g.strip() for g in raw.split(",") if g.strip()]

    def get_genre_matches(self, genres):
        if not genres:
            return self.data.copy()
        mask = pd.Series(False, index=self.data.index)
        for g in genres:
            pattern = rf"\b{re.escape(g)}\b"
            mask |= self.data["Genre"].astype(str).str.contains(pattern, case=False, na=False)
        return self.data.loc[mask].copy()

    def get_time_matches(self, df):
        raw = input("What's the max runtime (minutes)? (e.g., 90, 120): ").strip()
        try:
            max_min = float(raw)
        except ValueError:
            max_min = float("inf")
        if "Runtime" not in df.columns:
            return df
        return df[df["Runtime"].le(max_min)]

    def get_movie_date(self, df):
        ans = input("Modern only (2000–present)? y/n: ").strip().lower()
        year_col = "Released_Year"
        if ans == "y" and year_col in df.columns:
            return df[pd.to_numeric(df[year_col], errors="coerce").ge(2000)]
        return df

    def show_top(self, df, n=5):
        if df.empty:
            print("\nNo matches found. Try different filters!")
            return
        cols = [c for c in ["Series_Title", "Genre", "IMDB_Rating", "Meta_score", "Runtime", "Director", "Released_Year"] if c in df.columns]
        print("\nTop picks sorted by rating:")
        print(df[cols].sort_values(by="IMDB_Rating", ascending=False).head(n).to_string(index=False))

    def bye(self):
        print("\nHope you enjoy your movie!\nRemember to log it on Letterboxd!")

    def main(self):
        self.greet()
        genres = self.ask_genre()
        genre_matches = self.get_genre_matches(genres)
        time_matches = self.get_time_matches(genre_matches)
        final_matches = self.get_movie_date(time_matches)
        self.show_top(final_matches, n=3)
        self.bye()

if __name__ == "__main__":
    MovieRecs().main()
