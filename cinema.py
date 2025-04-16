
class City:
    def __init__(self, name):
        self.name = name


class Cinema:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.halls = []

    def get_name(self):
        return self.name

    def get_city(self):
        return self.city

    def add_hall(self, hall):
        self.halls.append(hall)

    def get_halls(self):
        return self.halls

    def get_movies(self):
        movies = set()
        for hall in self.halls:
            for show in hall.current_shows:
                movies.add(show.movie)

        return list(movies)


class Hall:
    def __init__(self, h_no, seats):
        self.no = h_no
        self.seats = seats
        self.current_shows = []

    def get_seats(self):
        return self.seats

    def schedule_show(self, sh_show):
        for show in self.current_shows:
            if show.st < sh_show.ed and show.ed > sh_show.st:
                return False

        self.current_shows.append(sh_show)
        return True

    def show_current_shows(self):
        print("-----------------------")
        for show in self.current_shows:
            print(show)
        print("-----------------------")

    def __repr__(self):
        return f"{self.no}"


class Seat:
    def __init__(self, seat_no, price):
        self.seat_no = seat_no
        self.price = price
