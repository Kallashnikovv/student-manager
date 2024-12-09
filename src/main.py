from src.student_manager import StudentManager
from src.attendance_manager import AttendanceManager
from src.storage_handler import StorageHandler

def main():
    s_manager = StudentManager()
    a_manager = AttendanceManager()
    storage_handler = StorageHandler()
    
    students_file = 'students.txt'
    attendance_file = 'attendance.txt'

    students = s_manager.import_students(storage_handler, students_file)
    print("Lista studentów:", students)

    s_manager.add_student(storage_handler, students_file, 'Jan Kowalski')
    s_manager.add_student(storage_handler, students_file, 'Julia Nowak')
    s_manager.add_student(storage_handler, students_file, 'Robert Lewandowski')
    s_manager.add_student(storage_handler, students_file, 'Szymon Piotrowski')
    
    students = s_manager.import_students(storage_handler, students_file)
    
    print("Lista studentów:", students)

    attendance = a_manager.manage_attendance()
    for student in students:
        a_manager.mark_attendance(attendance, student, True)

    a_manager.export_attendance(storage_handler, attendance_file, attendance)
    print("Lista obecności:", attendance)
    
    # Cleanup
    import os
    os.remove(students_file)
    os.remove(attendance_file)

# main()
