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