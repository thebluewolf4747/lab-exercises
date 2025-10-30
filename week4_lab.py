""" NUMBER GUESSING GAME """

def celsius_to_fahrenheit(celsius_temp):
    # converts a given temperature from celsius to fahrenheit
    fahrenheit = (celsius_temp * 9/5) + 32
    return fahrenheit

c_temp = 100
f_temp = celsius_to_fahrenheit(c_temp)
print(f"Celsius: {c_temp}, Fahrenheit: {f_temp}")


my_variable = "I am global"
def test_scope():
    my_variable = "I am local"
    print(my_variable)

test_scope()
print(my_variable)

"""
The first print statement (from inside the function) printed the value I am local as the print statement is part of the function that the variable it is printing is
stored in. The second print statement (outside the function) printed the value that is stored outside the function.
"""

# secret_number = 42

# while True:
#     user_guess = int(input("Guess the number: "))

#     if user_guess == secret_number:
        # print("Congratulations! You guessed it!")
    
#     elif user_guess < secret_number:
#         print("Too low! Try again.")

#     elif user_guess > secret_number:
#         print("Too high! Try again.")
