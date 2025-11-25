# list of students
students = []

# find student by name
def find_student(name: str):
    for i in students:
        if i["name"].lower() == name.lower():
            return i
    return None

# calculate average grade
def calculate_average(grades: list):
    if not grades:
        return None
    return sum(grades) / len(grades)

# add a new student
def add_student():
    name = input("Enter student name: ").strip()

    # checking for the student existence
    if find_student(name):
        print("This student already exists.")
        return
    # adding a student to the students list
    students.append({"name": name, "grades": []})
    print(f"Student '{name}' added.")

# add a grades for student
def add_grades():
    
    # select a student
    name = input("Enter student name: ")
    student = find_student(name)

    # checking for a student's existence
    if not student:
        print("Student not found.")
        return

    # infinite loop for adding grades
    while True:
        # getting a grade
        grade_input = input("Enter a grade (or 'done' to finish): ").strip()

        # stop entering grades
        if grade_input.lower() == "done":
            break

        # grade validation
        try:
            grade = int(grade_input)
            if 0 <= grade <= 100:
                student["grades"].append(grade)
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# print full report
def full_report():
    print("\n--- Student Report ---")

    # checking the avalibility of student
    if not students:
        print("No students found.")
        return

    # list of averages studentws grade
    averages = []

    # entering averages list
    for i in students:
        average_grade = calculate_average(i["grades"])
        if average_grade is None:
            print(f"{i['name']}'s average grade is N/A.")
        else:
            averages.append(average_grade)
            print(f"{i['name']}'s average grade is {average_grade:.1f}.")

    print("----------------------")

    # check for empty averages
    if not averages:
        print("No grades available to calculate summary.")
        return

    # print max, min, overall averag
    print(f"Max Average: {max(averages):.1f}")
    print(f"Min Average: {min(averages):.1f}")
    print(f"Overall Average: {sum(averages) / len(averages):.1f}")

# print top student info
def find_top_student():
    # check for empty students
    if not students:
        print("No students available.")
        return

    # list students with grades
    valid_students = [
        i for i in students if len(i["grades"]) > 0
    ]

    # if no students with grades
    if not valid_students:
        print("No grades available to determine top student.")
        return

    # find student with max average
    top_student = max(valid_students, key=lambda i: calculate_average(i["grades"]))
    # find top student average
    top_student_average = calculate_average(top_student["grades"])

    # print top student
    print(f"The top performer is {top_student['name']} with an average of {top_student_average:.1f}.")

# main def
def main():
    # infinite loop
    while True:
        # print menu
        print("\n--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Generate a full report")
        print("4. Find the top student")
        print("5. Exit program")

        # validation of user choice
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Enter a number from 1 to 5.")
            continue

        # cases for user choices
        match choice:
            case 1:
                add_student()
            case 2:
                add_grades()
            case 3:
                full_report()
            case 4:
                find_top_student()
            case 5:
                print("Exiting program.")
                break
            case _:
                print("Invalid option. Please choose 1-5.")

if __name__ == "__main__":
    main()
