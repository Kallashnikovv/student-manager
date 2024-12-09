import pytest
from src.attendance_manager import AttendanceManager
from tests.mock_storage_handler import MockStorageHandler

# setup_method - Used to initialize common objects before each test method

class TestAttendanceManager:
    def setup_method(self):
        self.storage_handler = MockStorageHandler()
        self.attendance_manager = AttendanceManager()
        self.file_path = 'attendance.txt'

    def test_manage_attendance(self):
        # When
        attendance = self.attendance_manager.manage_attendance()
        # Then
        assert attendance == {}

    def test_mark_attendance(self):
        # Given
        attendance = self.attendance_manager.manage_attendance()
        # When
        self.attendance_manager.mark_attendance(attendance, 'Anna Kowalska', True)
        self.attendance_manager.mark_attendance(attendance, 'Jan Nowak', False)
        # Then
        assert attendance == {'Anna Kowalska': True, 'Jan Nowak': False}

    def test_export_attendance(self):
        # Given
        attendance = {'Anna Kowalska': True, 'Jan Nowak': False}
        # When
        self.attendance_manager.export_attendance(self.storage_handler, self.file_path, attendance)
        # Then
        expected_output = ['Anna Kowalska: Obecny', 'Jan Nowak: Nieobecny']
        assert self.storage_handler.files[self.file_path] == expected_output

    def test_export_attendance_empty(self):
        # Given
        attendance = {}
        # When
        self.attendance_manager.export_attendance(self.storage_handler, self.file_path, attendance)
        # Then
        assert self.storage_handler.files[self.file_path] == []
