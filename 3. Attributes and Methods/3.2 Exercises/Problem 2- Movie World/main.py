from project.customer import Customer
from project.dvd import DVD
from project.movie_world import MovieWorld


customer = Customer('Atanas', 18, 123)
dvd = DVD('CONG: In the Wild', 555, 1998, 'August', 18)
dvd2 = DVD.from_date(777, 'CHE', '12.09.1988', 18)
# dvd.is_rented = True

movie_world = MovieWorld("Gaco")
movie_world.add_customer(customer)
movie_world.add_dvd(dvd)
movie_world.add_dvd(dvd2)

print(movie_world.rent_dvd(123, 555))
print(movie_world.rent_dvd(123, 555))
print(movie_world.return_dvd(123, 555))
print(movie_world.return_dvd(123, 555))
print(movie_world.rent_dvd(123, 777))

print(movie_world)
