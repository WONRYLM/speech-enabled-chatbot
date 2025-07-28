# class student_manager:  #Manage student records and storage
#     def __init__(self): # Initializing
#         self.student:list[Student_grading] = [] # Empty list of students
#         self.next_id = 1                        # Autoincrementing student id
#         self.load_student()
        
#         def load_student(self):                     #
#         try:
#             with open('students.json','r') as students: # Open the json file in read mode 
#                 data = json.load(students)              # Load data from the json file
#                 for student in data:
#                     try:
#                         student_id = data[Student_id]
#                         id = int(student_id[3:])        # Ensure 
#                         if id >= self.next_id:
#                             self.next_id = id + 1       #
#                         self.student.append(Student_grading(student_id = student_id))
#                     except (ValueError) as E:
#                         print(f"Error: {E}")
#         except FileNotFoundError :
#             print("Student File Does Not Exist")

#     def save_student(self):
#         with open('grades.csv','w') as after_grading:
#             fieldnames = ['Student ID','Student Name','Grade']
#             writer = csv.DictWriter(after_grading, fieldnames=fieldnames)



#  def add_student(self, name, marks):
#         """
#         Adds a new student to the list with an auto-generated ID and grade.
#         Saves the updated list to JSON.
#         """
#         grade = self.grading(marks)              # Get letter grade
#         student_id = self.generate_student_id()  # Generate unique ID
#         student = {
#             "id": student_id,
#             "name": name,
#             "marks": marks,
#             "grade": grade
#         }
#         self.students.append(student)            # Add student to the list
#         self.save_to_json()                      # Save updated list to JSON
#         print(f"Student {name} added with ID {student_id} and grade {grade}.")



  
# if __name__ == "__main__":
#     grading_system = StudentGrading()             # Create a grading system object
#     grading_system.add_student("Kevin", 85)       # Add a student with 85 marks
#     grading_system.add_student("Jane", 73)        # Add another student
#     grading_system.save_grades_to_csv()           # Save all students to CSV    
                    






    # Inputting student data   
def input_student_data(self):
    student_id = self.generate_student_id()
    student_name = input("Enter student name: ")
    try:
        marks = int(input("Enter student marks: "))
        if marks < 0 or marks >100 :
            print("Invalid. Please enter marks between 0 and 100")
            return
    except ValueError :
        print("Please enter a number!")  
        return  