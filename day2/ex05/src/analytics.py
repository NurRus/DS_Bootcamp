import os
from random import randint
import config

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

            # Пропускаем заголовок, если он есть
            if has_header:
                lines = lines[1:]

            data = [list(map(int, line.strip().split(','))) for line in lines]
            return data

    def struct_validate(self, lines, has_header):
        if has_header:
            if len(lines) < 2:
                return False
            header = lines[0].strip().split(',')
            if header != ['head', 'tail']:
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
            heads_count = sum(1 for row in self.data if row[0] == 1)
            tails_count = sum(1 for row in self.data if row[1] == 1)
            return heads_count, tails_count

        def fractions(self, heads, tails):
            total = heads + tails
            heads_fraction = (heads / total) * 100
            tails_fraction = (tails / total) * 100
            return heads_fraction, tails_fraction

    class Analytics(Calculations):
        def predict_random(self, n):
            predictions = []
            for _ in range(n):
                heads = randint(0, 1)
                tails = 1 - heads
                predictions.append([heads, tails])
            return predictions

        def predict_last(self):
            if self.data:
                return self.data[-1]
            else:
                return []

        def save_file(self, data, filename, extension='txt'):
            full_filename = f"{filename}.{extension}"
            with open(full_filename, 'w') as file:
                file.write(data)

        def generate_report(self, heads_count, tails_count, heads_fraction, tails_fraction, random_predictions):
            total_observations = heads_count + tails_count
            forecast_tails = sum(1 for prediction in random_predictions if prediction[1] == 1)
            forecast_heads = len(random_predictions) - forecast_tails

            report = config.REPORT_TEMPLATE.format(
                total_observations=total_observations,
                tails_count=tails_count,
                heads_count=heads_count,
                tails_fraction=tails_fraction,
                heads_fraction=heads_fraction,
                num_steps=len(random_predictions),
                forecast_tails=forecast_tails,
                forecast_heads=forecast_heads
            )
            return report
