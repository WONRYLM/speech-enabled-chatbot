# names = []
# marks = []
# for i in range (1,4):
#     x = input(f"ENTER NAME {i} : ")
#     y = int(input(f"ENTER YOUR MARKS :"))
#     names.append(x)
#     marks.append(y)
# for x in range(3):
#     print(names[x]+":",marks[x])

students = {}
subjects = ['Math', 'Kiswahili', 'English']

# Collecting the information for 5 students
for i in range(1, 6):
    sid = input(f"Enter Student ID {i}: ")
    name = input("Enter Name: ")
    
    # Creating an empty dictionary for marks
    marks = {}
    
    # Collecting marks for each subject
    for subject in subjects:
        mark = int(input(f"Enter marks for {subject}: "))
        marks[subject] = mark
    
    # Storing the student information in the dictionary
    students[sid] = {'name': name, 'marks': marks}

# To show the complete results for the students
for sid in students:
    info = students[sid]
    name = info['name']
    marks = info['marks']
    scores = []

    # Collect marks into a list
    for subject in marks:
        scores.append(marks[subject]) # Takes the marks with the corresponding subject and adds it to the scores list

    # Calculate stats
    total = sum(scores)
    average = total / len(scores)
    minimum = min(scores)
    maximum = max(scores)

    # Print student data with f-strings
    print(f"\nStudent ID: {sid}")  #\n - represents a new line
    print(f"Name: {name}")
    for subject in marks:          #Prints the subject and the corresponding mark
        print(f"{subject}: {marks[subject]}")
    print(f"Average Marks: {average}")
    print(f"Minimum Marks: {minimum}")
    print(f"Maximum Marks: {maximum}")
    
