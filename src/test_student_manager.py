import pytest
from student_manager import import_students, add_student
from mock_storage_handler import MockStorageHandler

# setup_method - Used to initialize common objects before each test method
# capsys - Captures output to stdout and stderr, useful for testing print statements

class TestStudentManager:
    def setup_method(self):
        self.storage_handler = MockStorageHandler()
        self.file_path = 'students.txt'

    def test_import_students(self):
        # Given
        self.storage_handler.files[self.file_path] = ['Anna Kowalska', 'Jan Nowak']
        # When
        students = import_students(self.storage_handler, self.file_path)
        # Then
        assert students == ['Anna Kowalska', 'Jan Nowak']

    def test_import_students_file_not_exist(self, capsys):
        # When
        students = import_students(self.storage_handler, self.file_path)
        # Then
        assert students == []
        captured = capsys.readouterr()
        assert f"File {self.file_path} does not exist. Creating a new file." in captured.out

    def test_add_student(self):
        # When
        add_student(self.storage_handler, self.file_path, 'Anna Kowalska')
        add_student(self.storage_handler, self.file_path, 'Jan Nowak')
        # Then
        assert self.storage_handler.files[self.file_path] == ['Anna Kowalska', 'Jan Nowak']

    def test_add_existing_student(self, capsys):
        # Given
        self.storage_handler.files[self.file_path] = ['Anna Kowalska']
        # When
        add_student(self.storage_handler, self.file_path, 'Anna Kowalska')
        # Then
        captured = capsys.readouterr()
        assert "Student Anna Kowalska already exists in the list." in captured.out
        assert self.storage_handler.files[self.file_path] == ['Anna Kowalska']
