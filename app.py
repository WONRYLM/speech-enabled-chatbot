
gradebook = {
    "Alice": {"Math": 85, "Science": 90, "History": 78},
    "Bob": {"Math": 72, "Science": 88, "History": 80},
    "Charlie": {"Math": 90, "Science": 85, "History": 85}
}
print("\nStudents who scored more than 80 in Science:")
for student, subjects in gradebook.items():
    if subjects["Science"] > 80:
        print(student)
