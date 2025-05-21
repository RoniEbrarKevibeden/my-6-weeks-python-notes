# TUPLES - Basics and Example Use Cases

# Define a tuple for a single student
student = ("Roni", 20, "Cybersecurity")

# Accessing tuple elements
print("Name:", student[0])
print("Age:", student[1])
print("Department:", student[2])

print("\n--- Student List ---")

#  List of tuples representing multiple students
students = [
    ("Roni", 20, "Cybersecurity"),
    ("Alice", 22, "Data Science"),
    ("Bob", 19, "AI Engineering")
]

# Loop through each student tuple and print info
for student in students:
    print("Name:", student[0])
    print("Age:", student[1])
    print("Department:", student[2])
    print("-----")
