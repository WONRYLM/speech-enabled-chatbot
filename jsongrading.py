import json #Importing the json module
import csv  #Importing the csv module   #To store the graded marks

class Student_grading:

    subjects = ['Math','English','Kiswahili']

    def __init__(self):  # Initializing
            self.students = []                           # Empty student list  
            self.file_json = 'students.json'             # Refers back to the json file for saving student data
            self.file_csv = 'students.csv'               # Refers back to the csv file for data storage
            self.load_student_data ()                    # Should load the students data
            
    def load_student_data(self):                        # Loads the existing students data from the json file
        try:    
            with open(self.file_json, 'r') as grading:  # Open the json file in read mode         
                self.students = json.load(grading)      # Reads the entire content of json file   
        except FileNotFoundError:                       # If the file does not exist // Error handling
            print("File does not exist")                # Print a message to the user
            # Handle missing or corrupted files
            self.students = []                          # If the file does not exist, set the students list to empty
            self.new_file()                             # Creates a new json file with an empty list if the original file is not found or corrupted
           
    def new_file(self):                                 # Creates a new json file with an empty list
        with open(self.file_json, 'w') as new_json_file:# Open the json file in write format
            json.dump([],new_json_file,indent = 4)      # Dump an empty list into the json file
    
    # Generating the student id
    def generate_student_id(self):
        return f"STU{len(self.students)+1:03d}"

    # Grading
    def grading(self,marks):
            
            if marks >= 90 :
                return "A"
            elif marks >= 80 :
                return "A-"
            elif marks >= 70 : 
                return "B+"
            elif marks >= 60 :
                return "B"
            elif marks >= 50 :
                return "C+"
            elif marks >= 40 :
                return "C"
            elif marks >= 30 :
                return "D+"
            elif marks >= 20 :
                return "D"
            else:
                return "F"
           
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

        grade = self.grading(marks)

        student_data = {"Student ID":student_id, "Student Name":student_name, "Marks":marks, "Grade":grade}

        self.students.append(student_data)

        print(f"{student_name} ({student_id}) scored a/an {grade} with {marks} ")

    
    # Saving data to CSV file    
    def save_grades_to_csv(self):                   # Saves the student data into a csv file   
        try:
            with open(self.file_csv, 'w', newline='') as csv_file: # Open the csv file in write mode
                csv_writer = csv.writer(csv_file)

                # Write the header row // Are the headings
                csv_writer.writerow(["Student ID","Student Name", "Grade", "Marks"])
                # Loops through each student in the list and writes their data in a row
                for student in self.students:
                    csv_writer.writerow([student['Student ID'], student['Student Name'], student['Marks'], student['Grade']])
                print(f"Grades saved to {self.file_csv} successfully!")  # Success message
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    grading_system = Student_grading()

    while True:
        print("\n1. Add new student")
        print("2. Save grades to CSV")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            grading_system.input_student_data()
        elif choice == '2':
            grading_system.save_grades_to_csv()
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")




                            

            
        

            # User to input data std name, std grade, 
            # grading automatically, 
            # auto-generate std id - STU001, 
            # save the graded marks into a csv file, 
            # menu to read the grades, add new students and edit marks
            # use classes and functions
            # should have many subjects