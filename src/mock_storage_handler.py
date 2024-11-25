class MockStorageHandler:
    def __init__(self):
        self.files = {}

    def read_file(self, file_path):
        content = self.files.get(file_path, None)
        if content is None:
            print(f"File {file_path} does not exist. Creating a new file.")
            self.files[file_path] = []
            return []
        else:
            return self.files[file_path][:]

    def write_file(self, file_path, lines):
        self.files[file_path] = lines[:]

    def append_to_file(self, file_path, line):
        if file_path in self.files:
            self.files[file_path].append(line)
        else:
            self.files[file_path] = [line]
