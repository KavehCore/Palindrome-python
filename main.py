# modules and global variables
import re


# normalize function
def normalize(text):
    return text.lower()


# core palindrome logic
def is_palindrome(text):
    normalized = normalize(text)

    if not normalized:
        return False
    return normalized == normalized[::-1]


# main function
def main():
    text = input("Enter a string: ")
    try:
        if is_palindrome(text):
            print("The string is a palindrome")
        else:
            print("The string is not a palindrome")
    except:
        print("Erorr")

# running the application
if __name__ == "__main__":
    main()