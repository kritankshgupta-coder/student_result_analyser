# Student Result Management System

A menu-driven command-line application in Python to store student records, calculate results and grades, and analyse class performance.

## Features

- Add, view, search, update marks of, and delete students
- Individual result: total, percentage, grade and PASS/FAIL
- Class analysis: total students, passed, failed, class average and topper
- Input validation (numbers only, marks between 0 and 100, no duplicate roll numbers)

## Project Structure

student_result_system/
├── main.py
├── student_manager.py
├── result_analysis.py
├── README.md
└── statement.md

## Requirements

- Python 3.7 or above (no external libraries needed)

## How to Run

bash
cd student_result_system
python main.py


## Menu Options

| Option | Action |
|--------|--------|
| 1 | Add Student |
| 2 | View All Students |
| 3 | Search Student |
| 4 | Update Student Marks |
| 5 | Delete Student |
| 6 | Show Result of a Student |
| 7 | Class Analysis |
| 8 | Exit |

## Grading Scheme

Each student has 5 subjects (100 marks each, 500 total). Percentage = total / 5.

| Percentage | Grade |
|------------|-------|
| 90 and above | A+ |
| 80 – 89 | A |
| 70 – 79 | B |
| 60 – 69 | C |
| 33 – 59 | D |
| Below 33 | Fail |

A student fails if any single subject is below 33, regardless of percentage, and the grade is then shown as "Fail".

## Limitations

- Data is stored in memory only and is lost when the program exits.

## Possible Improvements

- Save and load records using a file (JSON/CSV) or database
- Support a variable number of subjects
- Export results as a report