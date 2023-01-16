from cmath import pi
import math

# print(math.pi)

def sq_ft():
    ### Determine square footage based on user input. ###

    length = input("What is the LENGTH (in feet) of your room? ")
    width = input("What is the WIDTH (in feet) of your room? ")
    area = int(length) * int(width)

    print("Your Room is " + str(area) + " square feet.")

sq_ft()

def circle_circ():
    ### Calculate the circumference of a circle of given dimensions. ###
    radius = int(input("What is the RADIUS of your circle? "))

    circ = 2 * math.pi * radius

    print("Your circle's circumference is " + str(circ) + " units.")

circle_circ()