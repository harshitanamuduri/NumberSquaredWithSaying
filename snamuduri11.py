# Simple program that squares user-inputted numbers and displays a saying

def main():
    # Ask the user to input a number
    user_input = input("Enter a number: ")

    try:
        # Convert the input to a float (in case the user enters a decimal number)
        number = float(user_input)

        # Calculate the square of the number
        square_result = number ** 2

        # Display the result along with a saying
        print(f"The square of {number} is: {square_result}")
        print("Keep coding and learning!")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
