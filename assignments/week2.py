class Car:
    def __init__(self, color):
        self.color = color

my_car = Car('blue')

def crash(car1) :
    car1.color = 'burnt'

crash(Car('red'))
