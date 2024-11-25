from storage_handler import read_file, append_to_file

def import_students(file_path):
    students = read_file(file_path)
    return students

def add_student(file_path, student_name):
    students = read_file(file_path)
    if student_name not in students:
        append_to_file(file_path, student_name)
    else:
        print(f"Student {student_name} already exists in the list.")
