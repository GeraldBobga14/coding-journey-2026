print("Welcome to Grade Tracker \n")

print("1. Add Student \n" 
      "2. View Students \n" 
      "3. Show Average \n" 
      "4. Show Highest Grade\n" 
      "5. Exit \n")

list_of_students = []
list_of_grades = []

def student_name():
    name = input("Input Students Name: ")
    list_of_students.append(name)
    print("Student", name,  "has been added")
    grade = int(input("Input students grade: "))
    list_of_grades.append(grade)
    

def view_students():
    if list_of_students:
        for i in range(len(list_of_students)):
            print(list_of_students[i], "-", list_of_grades[i])
    else:
        print("There are no students here")

def show_average():
    total = sum(list_of_grades)
    average = total / len(list_of_grades)
    print("The average grade is:", average)

def main():
    choice = input("Selection an option : ")
    if choice == "1":
        student_name()
    elif choice == "2":
        view_students()
    elif choice == "3":
        show_average()
    else:
        print("Select another option.")

main()






