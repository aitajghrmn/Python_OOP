class Movie:
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director

        if type(duration) != int:
            raise TypeError("Duration must be integer")

        self.duration = duration

    def describe(self):
        print(f"{self.title} directed by {self.director}, duration: {self.duration} minutes")

    def is_long(self):
        if self.duration >= 120:
            return "This movie is long"
        else:
            return "This movie is not long"


def find_longest_movie(movies):
    longest = movies[0]

    for movie in movies:
        if movie.duration > longest.duration:
            longest = movie

    return longest


try:
    m1 = Movie("Movie1", "Director1", 90)
    m2 = Movie("Movie2", "Director2", 140)
    m3 = Movie("Movie3", "Director3", 120)

    movies = [m1, m2, m3]

    for movie in movies:
        movie.describe()
        print(movie.is_long())

    longest_movie = find_longest_movie(movies)
    longest_movie.describe()

except Exception as e:
    print(e)
