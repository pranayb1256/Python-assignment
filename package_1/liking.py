class Liking:
    def __init__(self, favorite_food, football_team, books, anime, favorite_place):
        self.favorite_food = favorite_food
        self.football_team = football_team
        self.books = books
        self.anime = anime
        self.favorite_place = favorite_place

    def display_liking(self):
        return (f"Favorite Food: {', '.join(self.favorite_food)}, "
                f"Favorite Football Team: {self.football_team}, "
                f"Favorite Books: {', '.join(self.books)}, "
                f"Favorite Anime: {', '.join(self.anime)}, "
                f"Favorite Place: {self.favorite_place}")
