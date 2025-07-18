def validate_age(age): 
    """
    Determine if the age entered is a positive integer. If not it prints a error message."""
    try:
        age = int(age) 
        if age <= 0: 
            raise ValueError("Age has to be a positive number") 
        return age # returns a number if the number is more than zero
    except ValueError:
            raise ValueError("Age must be a number")

age = input("Enter your age: ")
try:
    valid_age = validate_age(age)
    print(f"Your age is: {valid_age}")
except ValueError as e:
    print(f"Error: {e}")

import math
def calculate_rectangle_area(length, width):
     """multiply length and width"""
     return length * width
def calculate_circle_area(radius):
        """calculates the are of a circle which is πr^2""" 
        return math.pi * (radius ** 2)
def get_area(shape, *args):
     if shape == "rectangle":
          return calculate_rectangle_area(*args)
     elif shape == "circle":
          return calculate_circle_area(*args)
     else:
          raise ValueError("error: Please select a circle or rectangle")

shape = input("Do you want the area of a rectangle or circle? ").lower()
try:
    if shape == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = get_area("rectangle", length, width)
    elif shape == "circle":
        radius = float(input("Enter the radius of the circle: "))
        area = get_area("circle", radius)
    else:
        raise ValueError("Invalid shape selection.")

    print(f"The area of the {shape} is: {area:.2f}")

except ValueError as e:
    print(f"Error: {e}")