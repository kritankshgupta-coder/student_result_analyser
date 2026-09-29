# Problem Statement

## Title
Student Result Management System

## Problem
In many small institutions and classrooms, marks are still recorded and totalled by hand. This is slow and error-prone: totals and percentages get miscalculated, grades are applied inconsistently, records are hard to find or update, and there is no quick way to see how the whole class performed.

## Objective
To build a simple console application that lets a teacher manage student records and automatically produce accurate results and class-level statistics.

## Scope
The system will:
-Store student details (roll number, name, marks in 5 subjects).
-Allow adding, viewing, searching, updating and deleting records.
-Calculate total marks, percentage, grade and PASS/FAIL status for a student.
-roduce a class analysis: number of students, passed, failed, class average and topper.
-validate all input so that invalid data does not crash the program or corrupt records.

## Out of Scope
- Permanent storage (records exist only while the program runs)
- Graphical or web interface
- Multiple user accounts or login

## Users
Teachers or administrators who need to record and review student marks.

## Inputs and Outputs
- Input: menu choice, roll number, name, marks (0–100) for each subject
- Output: confirmation messages, student details, result sheet (total, percentage, grade, PASS/FAIL) and class summary

## Functional Requirements
ID Requirement
FR1 Add a student with a unique roll number and valid marks
FR2 View all students
FR3 Search a student by roll number
FR4 Update a student's marks
FR5 Delete a student
FR6 Show a student's result with grade and PASS/FAIL
FR7 Show class analysis including the topper

## Non-Functional Requirements
- Easy to use through a simple numbered menu
- Robust: handles invalid input without crashing
- Modular code split into three modules for readability and maintenance
- Runs on any system with Python 3, with no external dependencies

## Rules
- A student passes only if every subject is 33 or above.
- Grades: A+ (90+), A (80+), B (70+), C (60+), D (33+), Fail (below 33).

## Technology
Python 3 (standard library only)