#!/usr/bin/env python3
# Created By: Nathaniel
# Date: November, 2025
# Check if user can date grandchild.
def main():
    try:
        # Ask user for their age
        age = int(input("Please enter your age: "))

        # Check if user is in the required age range
        if age > 25 and age < 40:
            print(" You can date my grandchild")

        else:
            print(" You cant date my grandchild.")

    except ValueError:
        # if number input is not an integer
        print(" this is not an integer.")

    finally:
        print("thank you for playing")


if __name__ == "__main__":
    main()
