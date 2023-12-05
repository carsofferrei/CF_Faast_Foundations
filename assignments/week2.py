"""
Pylint Tutorial
"""

#pylint: disable=too-few-public-methods
class Car:
    """Creates a Car"""
    def __init__(self, color): 
        self.color = color


MY_CAR = Car('blue')

def crash(car1, car2): #pylint: disable=too-few-public-methods
    """An example function"""
    car1.color = 'burnt'

crash(Car('red'), MY_CAR)
