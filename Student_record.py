# Student Record Management System

# Empty Record 

record = []

# Record ADD Function

def add_student():
    roll_num = input("Enter Your Roll Number(i.e., 2025-BSCPE-**):  ")
    # Check if roll number already exists

    for student in record:
        if student["roll number"] == roll_num:
            return
# Validate name
    name = input("Enter the Name:  ")

    # validate age
    while True:
        age_input = input("Enter Age: ")
        if age_input.isdigit() and int(age_input) > 0:
            age = int(age_input)
            break
        print("Please enter a valid positive integer for age.")
        
    # get exactly 3 or more subjects in (tuple) and get their marks
    while True:
        subjects_input = input("Enter 3 Subjects (comma separated): ")
        subjects_list = [s.strip() for s in subjects_input.split(",") if s.strip()]

        if len(subjects_list) >= 3:
            subjects = tuple(subjects_list)
            marks = []
            for subject in subjects_list:
                mark = int(input(f"Enter marks of subject  {subject} (out of 100): "))
                marks.append(mark)
            break
        print("Please enter 3 or more subjects separated by commas.")

    # validate CGPA

    totm = sum(marks)
    cgpa = (totm / (len(marks) * 100)) * 4


# Making A Dictionary
    student = {
        "roll number": roll_num,
        "name": name,
        "age": age,
        "subjects": subjects,
        "cgpa": cgpa
    }      
    record.append(student)
    print("Student Record added Sucessfully!")


# Function to View Record
def view_students():

# Checking if there is any record in the list[]
    if not record:
        print("No student record found!!")
        return

# Printing the record
    roll = input("Enter The Roll Number to View Deatils of a student: ")     
    print("\nRoll No | Name | Age | Subjects | CGPA")
    print("-" * 60)
    found = False
    for student in record:
        if roll == "" or student["roll number"] == roll:
            found = True
            subjects_str = str(student['subjects'])
            print(f"{student['roll number']} | {student['name']} | {student['age']} | {subjects_str} | {student['cgpa']}")
    if not found:
        print("No student found with this roll number!\n")
        print()

# Record update Function
def update_student():
    roll = input("Enter roll number to update: ")
    for student in record:
        if student["roll number"] == roll:
            print("Leave field empty if you don't want to change it.")
            name = input(f"Enter new Name ({student['name']}): ") or student['name']
            # age
            age_input = input(f"Enter new Age ({student['age']}): ")
            age = int(age_input) if age_input and age_input.isdigit() else student['age']

            # subjects
            marks = []
            subjects_input = input(f"Enter new Subjects (comma separated) {student['subjects']}: ")
            if subjects_input != student["subjects"]:
                subjects_list = [s.strip() for s in subjects_input.split(",") if s.strip()]
                if len(subjects_list) >= 3:
                    subjects = tuple(subjects_list)

                    for subject in subjects_list:
                        mark = input(f"Enter marks of subject {subject} (out of 100): ")
                        marks.append(mark)
                else:
                    print("Invalid subjects input — keeping previous subjects.")
                    subjects = student['subjects']
            else:
                subjects = student['subjects']
            # CGPA
            cgpa = (sum(marks) / (len(marks) * 100)) * 4

            student.update({
                "name": name,
                "age": age,
                "subjects": subjects,
                "cgpa": cgpa
            })
            print("Student record updated successfully!\n")
            return
    print("No student found with this roll number!\n")           

# Deleting Record Function
def delete_student():
    roll = input("Enter roll number to delete: ")
    for student in record:
        if student["roll number"] == roll:
            record.remove(student)
            print("Student record deleted successfully!\n")
            return
    print("No student found with this roll number!\n")

# Main menu loop
while True:
    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting Student Management System. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.\n")
