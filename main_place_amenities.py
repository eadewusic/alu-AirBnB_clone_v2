#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models import *

# creation of a State
state = State(name="California")
state.save()

# creation of a City
city = City(state_id=state.id, name="San Francisco")
city.save()

# creation of a User
user = User(email="john@snow.com", password="johnpwd")
user.save()

# creation of 3 Places
place_0 = Place(user_id=user.id, city_id=city.id, name="House 0")
place_0.save()

place_1 = Place(user_id=user.id, city_id=city.id, name="House 1")
place_1.save()

place_bla = Place(user_id=user.id, city_id=city.id, name="House Bla")
place_bla.save()

place_2 = Place(user_id=user.id, city_id=city.id, name="Test House 2")
place_2.save()

# creation of 4 various Amenities
amenity_0 = Amenity(name="my_name_0")
amenity_0.save()

amenity_1 = Amenity(name="my_name_1")
amenity_1.save()

amenity_2 = Amenity(name="my_name_2")
amenity_2.save()

amenity_3 = Amenity(name="my_name_3")
amenity_3.save()

# link place_0 with 3 amenities
place_0.amenities.append(amenity_0)
place_0.amenities.append(amenity_1)
place_0.amenities.append(amenity_2)

# link place_1 with 1 amenity
place_1.amenities.append(amenity_1)

# link place_bla with 2 amenities
place_bla.amenities.append(amenity_2)
place_bla.amenities.append(amenity_3)

# Save the changes
storage.save()

print("OK")
