import sys
import os

class Research:
    def __init__(self, filepath):
        self.filename = filepath

    def file_reader(self):
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f"File {self.filename} does not exist")   
             
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            # Проверка структуры файла
            if not self.struct_validate(lines):
                raise ValueError("Invalid file structure")
            return ''.join(lines)
        
    def struct_validate(self, lines):
        if len(lines) < 2:
            return False
        header = lines[0].strip().split(',')
        if header != ['head','tail']:
            return False
        for line in lines[1:]:
            parts = line.strip().split(',')
            if len(parts) != 2:
                return False
            if parts[0] not in ['0', '1'] or parts[1] not in ['0', '1']:
                return False
            if parts[0] == parts[1]:
                return False
        return True
        

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("Usage: python first_constructor.py <path_to_file>")
    
    filepath = sys.argv[1]
    research = Research(filepath)
    try:
        content = research.file_reader()
        print(content)
    except (ValueError, FileNotFoundError, Exception) as e:
        print(e)
