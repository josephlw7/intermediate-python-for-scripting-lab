import string
import random

def random_password(length):
    """
    Generates a random password of specified length with uppercase, lowercase, and digits.
    """
    if length < 8:
        raise ValueError("Password must be at least 9 characters long.")

    # Define the sets of characters to use
    letters = string.ascii_letters  # Contains both uppercase and lowercase letters
    digits = string.digits          # Contains the digits 0-8
    symbols = string.punctuation    # Contains common punctuation symbols

    #Combine the values

    all_chars = letters + digits + symbols

    #Random character selection from all_chars

    password_chars = random.choices(all_chars, k=length)

    #The line before this will generate the pieces then combine with join.

    return ''.join(password_chars)

try:
    user_input = input("How long do you want your password? ")
    length = int(user_input)
    
    password = random_password(length)
    print("Here is your password:", password)

except ValueError:
    print("Please enter a valid number greater than 8.")

#Calculate the difference in days between the two dates and calculate the results.

import datetime

def day_diff(end_date, start_date):
     #Define the date format: YYYY-MM-DD
     date_format = "%Y-%m-%d"

     #convert the input string to a datetime object using datetime.strptime
     start_date = datetime.datetime.strptime(start_date, date_format)
     end_date = datetime.datetime.strptime(end_date, date_format)

     #return the result in days
     return abs((end_date - start_date).days)

# Get user input

try: 
     start_date = input("Please enter your start date (YYYY-MM-DD): ")
     end_date = input("Please enter your end date (YYYY-MM-DD): ")

    # Print the result
     result = day_diff(end_date, start_date)
     print("Number of days between dates:", result)

except ValueError:
     print("Invalid date format. Please enter dates in YYYY-MM-DD format.")

#3 calculate the area of a circle

import math

def calculate_circle_area(radius):
    """Calculates the area of a circle using πr^2""" 
    return math.pi * (radius ** 2)

try:
    radius = float(input("Enter the radius of the circle: "))
    area = calculate_circle_area(radius)
    print(f"The area of the circle is: {area:.2f}")
except ValueError:
    print("Invalid input")