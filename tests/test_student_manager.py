import pytest
from src.student_manager import StudentManager
from tests.mock_storage_handler import MockStorageHandler

# setup_method - Used to initialize common objects before each test method

class TestStudentManager:
    def setup_method(self):
        self.storage_handler = MockStorageHandler()
        self.student_manager = StudentManager()
        self.file_path = 'students.txt'

    def test_import_students(self):
        # Given
        self.storage_handler.files[self.file_path] = ['Anna Kowalska', 'Jan Nowak']
        # When
        students = self.student_manager.import_students(self.storage_handler, self.file_path)
        # Then
        assert students == ['Anna Kowalska', 'Jan Nowak']

    def test_import_students_file_not_exist(self):
        # When
        students = self.student_manager.import_students(self.storage_handler, self.file_path)
        # Then
        assert students == []

    def test_add_student(self):
        # When
        self.student_manager.add_student(self.storage_handler, self.file_path, 'Anna Kowalska')
        self.student_manager.add_student(self.storage_handler, self.file_path, 'Jan Nowak')
        # Then
        assert self.storage_handler.files[self.file_path] == ['Anna Kowalska', 'Jan Nowak']

    def test_add_existing_student(self):
        # Given
        self.storage_handler.files[self.file_path] = ['Anna Kowalska']
        # When / Then
        with pytest.raises(Exception):
            self.student_manager.add_student(self.storage_handler, self.file_path, 'Anna Kowalska')
        # Making sure the file content remains unchanged
        assert self.storage_handler.files[self.file_path] == ['Anna Kowalska']
