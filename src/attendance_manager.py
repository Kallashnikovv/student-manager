class AttendanceManager:
    def __init__(self):
        pass
    
    def manage_attendance(self):
        attendance = {}
        return attendance

    def mark_attendance(self, attendance, student_name, is_present):
        attendance[student_name] = is_present

    def export_attendance(self, storage_handler, file_path, attendance):
        lines = []
        for student, status in attendance.items():
            lines.append(f"{student}: {'Obecny' if status else 'Nieobecny'}")
        try:
            storage_handler.write_file(file_path, lines)
        except IOError as e:
            raise IOError(f"Unable to write to file '{file_path}': {e}")
