def manage_attendance():
    attendance = {}
    return attendance

def mark_attendance(attendance, student_name, is_present):
    attendance[student_name] = is_present

def export_attendance(storage_handler, file_path, attendance):
    lines = []
    for student, status in attendance.items():
        lines.append(f"{student}: {'Obecny' if status else 'Nieobecny'}")
    storage_handler.write_file(file_path, lines)
