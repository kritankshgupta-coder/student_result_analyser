NUM_SUBJECTS = 5
MAX_MARKS = 100

students = []


def get_int(prompt, min_value=None, max_value=None):
    """Keep asking until the user enters a valid integer in range."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if min_value is not None and value < min_value:
            print(f"Value must be at least {min_value}.")
        elif max_value is not None and value > max_value:
            print(f"Value must be at most {max_value}.")
        else:
            return value


def get_marks(prefix="Enter"):
    """Read marks for all subjects, validated between 0 and MAX_MARKS."""
    return [
        get_int(f"{prefix} marks of subject {i} (0-{MAX_MARKS}): ", 0, MAX_MARKS)
        for i in range(1, NUM_SUBJECTS + 1)
    ]


def find_student(roll):
    """Return the student dict with this roll number, or None."""
    for s in students:
        if s["roll"] == roll:
            return s
    return None


def add_student():
    roll = get_int("Enter roll number: ", 1)
    if find_student(roll):
        print("A student with this roll number already exists.")
        return

    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    students.append({"roll": roll, "name": name, "marks": get_marks()})
    print("Student added successfully!")


def view_students():
    if not students:
        print("No student records found.")
        return
    for s in students:
        print(f"Roll No: {s['roll']}  Name: {s['name']}  Marks: {s['marks']}")


def search_student():
    roll = get_int("Enter roll number to search: ", 1)
    s = find_student(roll)
    if s is None:
        print("Student not found.")
        return
    print("Roll No:", s["roll"])
    print("Name:", s["name"])
    print("Marks:", s["marks"])


def update_student():
    roll = get_int("Enter roll number to update: ", 1)
    s = find_student(roll)
    if s is None:
        print("Student not found.")
        return
    s["marks"] = get_marks("Enter new")
    print("Marks updated successfully!")


def delete_student():
    roll = get_int("Enter roll number to delete: ", 1)
    s = find_student(roll)
    if s is None:
        print("Student not found.")
        return
    students.remove(s)
    print("Student deleted successfully!")