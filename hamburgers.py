# IS 303-003
# Team 8
# Ian Purnell, Allan Foote, Grant Alston, Keller Elison, Michael Spotts
# 3/4/23
# Hamburger Order Tracker (Group Project)

# import necessary functions
from math import random

# classes
class Order :
    def __init__(self):
        self.burger_count = 0

    def randomBurgers(self):
        iRandomBurger = random.randint(1, 20)
        return(iRandomBurger)