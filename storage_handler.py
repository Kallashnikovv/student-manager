def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
        return [line.strip() for line in content]
    except FileNotFoundError:
        print(f"File {file_path} does not exist. Creating a new file.")
        with open(file_path, 'w') as file:
            pass
        return []

def write_file(file_path, lines):
    with open(file_path, 'w') as file:
        for line in lines:
            file.write(f"{line}\n")

def append_to_file(file_path, line):
    with open(file_path, 'a') as file:
        file.write(f"{line}\n")
