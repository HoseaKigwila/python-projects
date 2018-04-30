class cyberplant:
    def __init__(self, name):
        self.name = name
        self.health = 70
        self.water = 10

    def watering(self, plant):
        plant.health += self.water

    def forget(self,plant):
        plant.health -= 20
    print ("blue lost 20 points since you forgot to water the plant")

    def __str__(self):
        return "{} current health is {}".format(self.name, self.health)


bluebells = cyberplant("bluebells")
bluebells.watering(bluebells)
bluebells.forget(bluebells)
print (bluebells.health)
print (bluebells)
