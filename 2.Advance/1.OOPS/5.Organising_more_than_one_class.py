from rocket import Rocket, Rocketboard

boardOfRockets = Rocketboard(4)

myRocket = Rocket(altitude=10, x=4)
anotherRocket = Rocket()

# print(boardOfRockets)/

# boardOfRockets[0].x = 
# print(Rocketboard.get_distance(myRocket, anotherRocket))


print(len(boardOfRockets))
print(boardOfRockets.get_amount_of_rockets())
