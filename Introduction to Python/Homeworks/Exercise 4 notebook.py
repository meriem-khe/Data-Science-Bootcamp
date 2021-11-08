#Write a Python class named Rectangle constructed by a length and width and
# a method which will compute the area of a rectangle.

class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width  = width

    def area(self):
        return self.length*self.width

newRectangle = Rectangle(14,9)
print(newRectangle.area())


#Create a Vehicle class without any variables and methods.

class Vehicle:
    pass

#Create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

car = Vehicle(230,20)
print(car.max_speed, car.mileage)



#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Bus(Vehicle):
    pass

object=Bus(240,22)
print(object.max_speed,object.mileage)