import csv

""" Exercise 1 """
def entry(file):
    with open(file, "a") as file:
        entry = input("Enter your diary entry here: ")
        file.write(entry + "\n")
    return file

def read(file):
    with open(file, "r") as file:
        contents = file.read()
        file.close()
    return contents

# entry("Text Files/diary.txt")
# entry("Text Files/diary.txt")
# print(read("Text Files/diary.txt"))
""" Exercise 2 """
grades = {
    "Alice" : [85, 90, 92],
    "Bob" : [78, 81, 85],
    "Charlie" : [95, 100, 98]
}

def create_gradebook():
    list1 = ["Name", "Score 1", "Score 2", "Score 3"]
    with open("Text Files/grades.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(list1)
        for student, scores in grades.items():
            writer.writerow([student] + scores) # e.g., ['Bob', 85, 90]

# create_gradebook()

def calc_average():
    with open("Text Files/grades.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        
        for row in reader:
            name = row[0]
            scores = [float(x) for x in row[1:]]  # everything after the name
            avg_score = sum(scores) / len(scores)
            return f"{name} - Average Score: {avg_score}"

calc_average()

