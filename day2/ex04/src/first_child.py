import sys
import os
from random import randint

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

        def __init__(self, data):
            self.data = data

        def counts(self):
            head_count = sum(1 for row in self.data if row[0] == 1)
            tail_count = sum(1 for row in self.data if row[1] == 1)
            return head_count, tail_count
        
        def fractions(self, heads, tails):
            total = heads + tails
            heads_fraction = 100 * (heads / total)
            tails_fraction = 100 * (tails / total)
            return heads_fraction, tails_fraction
        
    class Analytics(Calculations):

        def predict_random(self, n):
            predict = []
            for _ in range(n):
                head = randint(0, 1)
                tails = 1 - head
                predict.append([head, tails])
            return predict
        
        def predict_last(self):
            if self.data:
                return self.data[-1]
            else:
                return []
        

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("Usage: python first_constructor.py <path_to_file>")
    
    filepath = sys.argv[1]
    research = Research(filepath)
    try:
        data = research.file_reader(has_header=True)
        print(data)

        calculations = Research.Calculations(data)
        heads_count, tails_count = calculations.counts()
        print(heads_count, tails_count)

        heads_fraction, tails_fraction = calculations.fractions(heads_count, tails_count)
        print(heads_fraction, tails_fraction)

        analytics = Research.Analytics(data)
        random_predict = analytics.predict_random(3)
        print(random_predict)

        last_predict = analytics.predict_last()
        print(last_predict)
        
    except (ValueError, FileNotFoundError, Exception) as e:
        print(e)
