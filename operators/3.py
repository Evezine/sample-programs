#3.	  Write a Python program that calculates the area of a circle based on the radius 
    # Sample Output :
    # r = 1.1
    # Area = 3.8013271108436504


# Import the 'pi' constant from the 'math' module to calculate the area of a circle
from math import pi

r=float(input("Enter the radius of the circle:"))

# Calculate the area of the circle using the formula: area = π * r^2
area= pi * r ** 2

print ("the area of a circle with radius " + str(r) + "is:" + str(area))