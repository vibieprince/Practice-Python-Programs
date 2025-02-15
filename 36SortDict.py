# List of dictionaries
students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 75},
    {"name": "Charlie", "marks": 95},
    {"name": "David", "marks": 65}
]

# Sorting by 'marks' using lambda function
sorted_students = sorted(students, key=lambda x: x["marks"])

# Display sorted list
for student in sorted_students:
    print(student)
