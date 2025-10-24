""" This program contains all week 2 lab exercises. """

running = True
while running:
    temp = int(input("Type a temperature to convert from Celsius to Fahrenheit: "))
    if temp == -100000000000:
        running = False
        break
    fahrenheit = (temp * 9/5) + 32      # Formula converting celsius to fahrenheit
    print(f"Celsius: {temp}, Fahrenheit: {fahrenheit}") # prints both temperature values

""" Increasing the celsius value increases the fahrenheit value. """

string = "String example"
integer = 10
float = 15.6
boolean = True

print(type(string))
print(type(integer))
print(type(float))
print(type(boolean))


float = ""
print(type(float))

# variable types are checked at runtime and not during compilation


name = "Rayyan"
course = "Computer Science"
fav_language = "Python"

greeting1 = "H" + "e" + "l" + "l" + "o"
greeting2 = "Hello, my name is {name}".format(name=name)
greeting3 = f"Hello, my name is {name}"

hello = "Hello"
print(f"{hello:<10}World")

try:
    user_age = int(input("What is your age? "))
    if user_age < 13:
        print("You are a child")
    else:
        print("You are not a child")
except ValueError:
    print("Not the right data type!")