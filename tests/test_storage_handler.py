import pytest

from src.storage_handler import StorageHandler

# setup_method - Used to initialize common objects before each test method

# tmp_path - Provided by pytest to create temporary directories and files
# for testing actual file operations without affecting the real file system.

class TestStorageHandler:
    def setup_method(self):
        self.storage_handler = StorageHandler()

    def test_read_file(self, tmp_path):
        # Given
        test_file = tmp_path / 'test.txt'
        test_file.write_text('Line1\nLine2\n')
        # When
        content = self.storage_handler.read_file(test_file)
        # Then
        assert content == ['Line1', 'Line2']

    def test_read_file_not_exist(self, tmp_path):
        # Given
        test_file = tmp_path / 'nonexistent.txt'
        # When
        content = self.storage_handler.read_file(test_file)
        # Then
        assert content == []
        assert test_file.exists()

    def test_write_file(self, tmp_path):
        # Given
        test_file = tmp_path / 'test.txt'
        lines = ['Line1', 'Line2']
        # When
        self.storage_handler.write_file(test_file, lines)
        # Then
        with open(test_file, 'r') as file:
            content = file.readlines()
        assert [line.strip() for line in content] == lines

    def test_append_to_file(self, tmp_path):
        # Given
        test_file = tmp_path / 'test.txt'
        test_file.write_text('Line1\n')
        # When
        self.storage_handler.append_to_file(test_file, 'Line2')
        # Then
        with open(test_file, 'r') as file:
            content = file.readlines()
        assert [line.strip() for line in content] == ['Line1', 'Line2']
