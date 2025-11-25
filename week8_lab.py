""" Exercise 1 """

# 1. Create a List of Dictionaries
# This reperesents a database of students
students = [
    {"name": "Alice", "score": 85, "passed": True},
    {"name": "Bob", "score": 40, "passed": False},
    {"name": "Charlie", "score": 92, "passed": True}
]

# 2. The loop
# 'student' is a temporary variable that holds ONE dictionary at a time.
print("--- Class Results ---")

for student in students:
    # 3. Access specific data using the ["keys"]
    name = student["name"]
    score = student["score"]

    # 4. Print it nicely
    print(f"Student: {name} | Score: {score}")
    if student["passed"] == True:
        print("Status: Pass")
    else:
        print("Status: Fail")

print("---------------------")


""" Exercise 2 """

products = [
    {"item": "Apple", "price": 0.50},
    {"item": "Bread", "price": 1.20},
    {"item": "Milk", "price": 0.90},
]

print("--- Price List ---")
for product in products:
    item = product["item"]
    price = product["price"]

    print(f"The price of {item} is £{price}.")
