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

entry("Diary Entries/diary.txt")
entry("Diary Entries/diary.txt")
print(read("Diary Entries/diary.txt"))