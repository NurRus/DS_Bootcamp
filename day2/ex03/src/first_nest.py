import sys
import os

class Research:
    def __init__(self, filepath):
        self.filename = filepath

    def file_reader(self, has_header=True):
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f"File {self.filename} does not exist")   
             
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            # Проверка структуры файла
            if not self.struct_validate(lines, has_header):
                raise ValueError("Invalid file structure")
            
            if has_header:
                lines = lines[1:]
            
            data = [list(map(int, line.strip().split(','))) for line in lines]
            return data
        
    def struct_validate(self, lines, has_header):
        if has_header:
            if len(lines) < 2:
                return False
            header = lines[0].strip().split(',')
            if header != ['head','tail']:
                return False
            lines = lines[1:]

        for line in lines:
            parts = line.strip().split(',')
            if len(parts) != 2:
                return False
            if parts[0] not in ['0', '1'] or parts[1] not in ['0', '1']:
                return False
            if parts[0] == parts[1]:
                return False
        return True
    
    class Calculations:
        @staticmethod
        def counts(data):
            head_count = sum(1 for row in data if row[0] == 1)
            tail_count = sum(1 for row in data if row[1] == 1)
            return head_count, tail_count
        
        @staticmethod
        def fractions(heads, tails):
            total = heads + tails
            heads_fraction = 100 * (heads / total)
            tails_fraction = 100 * (tails / total)
            return heads_fraction, tails_fraction
        

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("Usage: python first_constructor.py <path_to_file>")
    
    filepath = sys.argv[1]
    research = Research(filepath)
    try:
        data = research.file_reader(has_header=True)
        print(data)

        heads_count, tails_count = Research.Calculations.counts(data)
        print(heads_count, tails_count)

        heads_fraction, tails_fraction = Research.Calculations.fractions(heads_count, tails_count)
        print(heads_fraction, tails_fraction)
        
    except (ValueError, FileNotFoundError, Exception) as e:
        print(e)
