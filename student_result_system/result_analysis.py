from student_manager import students, find_student, get_int, NUM_SUBJECTS

PASS_MARK = 33


def calculate_percentage(marks):
    return sum(marks) / len(marks)


def has_failed(marks):
    """A student fails if any subject is below the pass mark."""
    return any(m < PASS_MARK for m in marks)


def calculate_grade(percentage, failed=False):
    # Fixed: grade now agrees with PASS/FAIL (original could show grade D but result FAIL)
    if failed:
        return "Fail"
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= PASS_MARK:
        return "D"
    return "Fail"


def show_result():
    roll = get_int("Enter roll number: ", 1)
    s = find_student(roll)
    if s is None:
        print("Student not found.")
        return

    marks = s["marks"]
    total = sum(marks)
    percentage = calculate_percentage(marks)
    failed = has_failed(marks)

    print("Name:", s["name"])
    print(f"Total Marks: {total} out of {NUM_SUBJECTS * 100}")
    print(f"Percentage: {percentage:.2f}%")
    print("Grade:", calculate_grade(percentage, failed))
    print("Result:", "FAIL" if failed else "PASS")


def class_analysis():
    if not students:
        print("No students added yet.")
        return

    pass_count = sum(1 for s in students if not has_failed(s["marks"]))
    fail_count = len(students) - pass_count
    topper = max(students, key=lambda s: calculate_percentage(s["marks"]))
    average = sum(calculate_percentage(s["marks"]) for s in students) / len(students)

    print("Total Students:", len(students))
    print("Passed:", pass_count)
    print("Failed:", fail_count)
    print(f"Class Average: {average:.2f}%")
    print(f"Topper: {topper['name']} with {calculate_percentage(topper['marks']):.2f}%")
