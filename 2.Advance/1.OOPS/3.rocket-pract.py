from random import randint

class Rocket:

    def __init__(self):
        self.altitude = 0

    def move_up(self):
        self.altitude += 1

rockets = [Rocket() for __ in range(10)]

# print(rockets)

for __ in range(10):
    rocketIndexTomove = randint(0,len(rockets)-1)
    rockets[rocketIndexTomove].move_up()

for rocket in rockets:
    print(rocket.altitude)