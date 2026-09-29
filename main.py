from student_manager import (add_student, view_students, search_student, update_student, delete_student, get_int)
from result_analysis import show_result, class_analysis

ACTIONS = {
    1: add_student,
    2: view_students,
    3: search_student,
    4: update_student,
    5: delete_student,
    6: show_result,
    7: class_analysis,
}


def print_menu():
    print("\nSTUDENT RESULT MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Show Result of a Student")
    print("7. Class Analysis")
    print("8. Exit")


def main():
    while True:
        print_menu()
        choice = get_int("Enter your choice: ")
        if choice == 8:
            print("Thank you! Exiting program.")
            break
        action = ACTIONS.get(choice)
        if action:
            action()
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()