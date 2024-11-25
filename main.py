from student_manager import import_students, add_student
from attendance_manager import manage_attendance, mark_attendance, export_attendance

def main():
    students_file = 'students.txt'
    attendance_file = 'attendance.txt'

    students = import_students(students_file)
    print("Lista studentów:", students)

    add_student(students_file, 'Jan Kowalski')
    add_student(students_file, 'Julia Nowak')
    add_student(students_file, 'Robert Lewandowski')
    add_student(students_file, 'Szymon Piotrowski')

    attendance = manage_attendance()
    for student in students:
        mark_attendance(attendance, student, True)

    export_attendance(attendance_file, attendance)
    print("Lista obecności:", attendance)

main()
