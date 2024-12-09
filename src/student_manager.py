from src.exceptions import StudentExistsError

class StudentManager:
    def __init__(self):
        pass
    
    def import_students(self, storage_handler, file_path):
        students = storage_handler.read_file(file_path)
        return students

    def add_student(self, storage_handler, file_path, student_name):
        try:
            students = storage_handler.read_file(file_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{file_path}' does not exist.")
        if student_name not in students:
            storage_handler.append_to_file(file_path, student_name)
        else:
            raise StudentExistsError(f"Student {student_name} already exists in the list.")
            
