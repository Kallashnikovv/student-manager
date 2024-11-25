def import_students(storage_handler, file_path):
    students = storage_handler.read_file(file_path)
    return students

def add_student(storage_handler, file_path, student_name):
    students = storage_handler.read_file(file_path)
    if student_name not in students:
        storage_handler.append_to_file(file_path, student_name)
    else:
        print(f"Student {student_name} already exists in the list.")
