from booking_system import BookingSystem
from cinema import City, Cinema, Hall, Seat
from movie import Movie, Catalog
from notification import SmsNotification
from show import Show

ob1 = SmsNotification()

catalog = Catalog()

m1 = Movie('Kuch kuch hota h', 'hindi', [ob1])
m2 = Movie('Dark Knight', 'english', [ob1])
m3 = Movie('Maharaja', 'Telugu', [ob1])

catalog.add_movie(m1)
catalog.add_movie(m2)
catalog.add_movie(m3)

city1 = City('Prayagraj')

cin1 = Cinema('C1', city1)
s1 = Seat(1, 100)
s2 = Seat(2, 150)
s3 = Seat(3, 200)
hall1 = Hall(1, [s1, s2, s3])
cin1.add_hall(hall1)

cin2 = Cinema('C2', city1)
s4 = Seat(1, 100)
s5 = Seat(2, 250)
s6 = Seat(3, 600)
hall2 = Hall(1, [s4, s5, s6])
cin2.add_hall(hall2)

print(catalog.get_movies_by_title('Dark Knight'))
print(catalog.get_movie_by_lang('Telugu'))

show1 = Show(1, 3, hall1, m1)
sl1 = show1.create_slot(s1)
sl2 = show1.create_slot(s2)

show2 = Show(4, 6, hall1, m2)
sl3 = show2.create_slot(s2)
sl4 = show2.create_slot(s3)

show3 = Show(3, 4, hall1, m3)
sl5 = show3.create_slot(s1)
sl6 = show3.create_slot(s2)
sl7 = show3.create_slot(s3)

hall1.show_current_shows()

booking_system = BookingSystem()
booking1 = booking_system.book('B1', show1, [sl1, sl2])

print(booking1)

hall1.show_current_shows()

booking_system.cancel_booking(booking1)

hall1.show_current_shows()

print(booking1)



