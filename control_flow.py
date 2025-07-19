#Write a function with a logical name of your choice. It should:
#Take a number as input
#Check if the number is a prime number using a for loop and appropriate conditional statements

def is_prime_number(number):
    """
    Checks if a given number is a prime number.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Example usage
num = 17
if is_prime_number(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

num = 15
if is_prime_number(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

#Write a function with a logical name of your choice. It should:
#Take a dictionary as input
#Write a loop that iterates through the dictionary and prints both the key and the value for each item
#Optionally, explore different ways to iterate (for example, using .items(), .keys(), and .values())

def print_dictionary_items(input_dictionary):
    """
    Iterates through a dictionary and prints each key-value pair.

    Args:
        input_dictionary: The dictionary to iterate through.
    """
    print("Iterating using .items():")
    for key, value in input_dictionary.items():
        print(f"Key: {key}, Value: {value}")

    print("\nIterating using .keys() and indexing:")
    for key in input_dictionary.keys():
        print(f"Key: {key}, Value: {input_dictionary[key]}")

    print("\nIterating using implicit key iteration:")
    for key in input_dictionary:
        print(f"Key: {key}, Value: {input_dictionary[key]}")

# Example usage:
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print_dictionary_items(my_dict)

#Write a function with a logical name of your choice. It should:
#Take a number as input
#Include error handling to ensure the number provided is a positive integer
#Use a while loop to print numbers from 1 to n, where n is the number provided by the user

def print_numbers_from_one_to_n(n):
    """
    Prints numbers from 1 to n (inclusive) using a while loop.
    Includes error handling to ensure n is a positive integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be a positive integer.")
    if n <= 0:
        raise ValueError("Input must be a positive integer.")

    count = 1
    while count <= n:
        print(count)
        count += 1

# Get input from the user and handle potential errors
while True:
    try:
        user_input = int(input("Enter a positive integer: "))
        print_numbers_from_one_to_n(user_input)
        break  # Exit the loop if input is valid
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
    except TypeError as e:
        print(e)
        break