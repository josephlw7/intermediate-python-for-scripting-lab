#Create a funtion with a logical name of choice
#Read the text file
#Counts the number of words in the text file
#Handle potential FileNotFoundError exceptions gracefully

#Define the function

def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

#use the test.txt file
word_count = count_words_in_file("sample.txt")

if word_count is not None:
    print(f"The file contains {word_count} words.")


#Write a function with a logical name of your choice
#Take a list of strings
#Write each string to a new line in a file named output.txt

def write_lines(lines):
    with open("output.txt", "w") as file:
        for line in lines:
            file.write(line + "\n")

#input list below... rewrites output.txt
my_list = ["First line", "Second line", "Third line"]
write_lines(my_list)