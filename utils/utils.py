def load_json(file_path):
    import json
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    import json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_text_file(content, file_path):
    with open(file_path, 'w') as file:
        file.write(content)

def format_string(s):
    return s.strip().capitalize()