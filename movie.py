class Movie:
    def __init__(self, title, language, observers):
        self.title = title
        self.lang = language
        self.shows = []
        self.observers = observers
        self.notify()

    def get_title(self):
        return self.title

    def add_show(self, show):
        self.shows.append(show)

    def __repr__(self):
        return f"({self.title} - {self.lang})"

    def notify(self):
        for observer in self.observers:
            observer.update(F"New Notification - {self.title} movie is Released. Go Watch !!!")


class Catalog:
    def __init__(self):
        self.movie_by_title = {}
        self.movie_by_lang = {}

    def add_movie(self, movie):
        if movie.title not in self.movie_by_title:
            self.movie_by_title[movie.title] = set()
        if movie.lang not in self.movie_by_lang:
            self.movie_by_lang[movie.lang] = set()

        self.movie_by_title[movie.title].add(movie)
        self.movie_by_lang[movie.lang].add(movie)

    def get_movies_by_title(self, title, movie_set=set()):
        if title not in self.movie_by_title:
            return set()
        else:
            movies = self.movie_by_title[title]
            if movie_set:
                movies = movies.intersection(movie_set)

            return movies

    def get_movie_by_lang(self, lang, movie_set=set()):
        if lang not in self.movie_by_lang:
            return set()
        else:
            movies = self.movie_by_lang[lang]
            if movie_set:
                movies = movies.intersection(movie_set)

            return movies
