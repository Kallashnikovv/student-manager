import pytest
from attendance_manager import manage_attendance, mark_attendance, export_attendance
from mock_storage_handler import MockStorageHandler

# setup_method - Used to initialize common objects before each test method

class TestAttendanceManager:
    def setup_method(self):
        self.storage_handler = MockStorageHandler()
        self.file_path = 'attendance.txt'

    def test_manage_attendance(self):
        # When
        attendance = manage_attendance()
        # Then
        assert attendance == {}

    def test_mark_attendance(self):
        # Given
        attendance = manage_attendance()
        # When
        mark_attendance(attendance, 'Anna Kowalska', True)
        mark_attendance(attendance, 'Jan Nowak', False)
        # Then
        assert attendance == {'Anna Kowalska': True, 'Jan Nowak': False}

    def test_export_attendance(self):
        # Given
        attendance = {'Anna Kowalska': True, 'Jan Nowak': False}
        # When
        export_attendance(self.storage_handler, self.file_path, attendance)
        # Then
        expected_output = ['Anna Kowalska: Obecny', 'Jan Nowak: Nieobecny']
        assert self.storage_handler.files[self.file_path] == expected_output

    def test_export_attendance_empty(self):
        # Given
        attendance = {}
        # When
        export_attendance(self.storage_handler, self.file_path, attendance)
        # Then
        assert self.storage_handler.files[self.file_path] == []
