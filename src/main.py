from student_manager import import_students, add_student
from attendance_manager import manage_attendance, mark_attendance, export_attendance
import storage_handler

def main():
    students_file = 'students.txt'
    attendance_file = 'attendance.txt'

    students = import_students(storage_handler, students_file)
    print("Lista studentów:", students)

    add_student(storage_handler, students_file, 'Jan Kowalski')
    add_student(storage_handler, students_file, 'Julia Nowak')
    add_student(storage_handler, students_file, 'Robert Lewandowski')
    add_student(storage_handler, students_file, 'Szymon Piotrowski')
    
    students = import_students(storage_handler, students_file)
    
    print("Lista studentów:", students)

    attendance = manage_attendance()
    for student in students:
        mark_attendance(attendance, student, True)

    export_attendance(storage_handler, attendance_file, attendance)
    print("Lista obecności:", attendance)

# main()
