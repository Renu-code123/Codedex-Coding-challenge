## PI DAY
import math

def cut_pie(diameter, friends):
    circumference = math.pi * diameter
    crust_per_friend = circumference / friends
    return round(crust_per_friend, 2)
