import os
from random import randint
import config
import logging
import requests

# Настройка логирования
logging.basicConfig(filename='analytics.log', level=logging.INFO,
                    format='%(asctime)s %(message)s')

class Research:
    def __init__(self, filepath):
        self.filename = filepath
        logging.info(f"Initialized Research with filepath: {filepath}")

    def file_reader(self, has_header=True):
        logging.info("Reading file data")
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
            logging.info(f"File data read successfully: {data}")
            return data

    def struct_validate(self, lines, has_header):
        logging.info("Validating file structure")
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
        logging.info("File structure is valid")
        return True
    
    def send_telegram_message(self, message):
        logging.info(f"Sending Telegram message: {message}")
        url = f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": config.TELEGRAM_CHANNEL_ID,
            "text": message
        }
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            logging.info("Telegram message sent successfully")
        else:
            logging.error(f"Failed to send Telegram message: {response.text}")

    class Calculations:
        def __init__(self, data):
            self.data = data
            logging.info(f"Initialized Calculations with data: {data}")

        def counts(self):
            logging.info("Calculating the counts of heads and tails")
            heads_count = sum(1 for row in self.data if row[0] == 1)
            tails_count = sum(1 for row in self.data if row[1] == 1)
            logging.info(f"Counts calculated: heads={heads_count}, tails={tails_count}")
            return heads_count, tails_count

        def fractions(self, heads, tails):
            logging.info("Calculating the fractions of heads and tails")
            total = heads + tails
            heads_fraction = (heads / total) * 100
            tails_fraction = (tails / total) * 100
            logging.info(f"Fractions calculated: heads={heads_fraction:.2f}%, tails={tails_fraction:.2f}%")
            return heads_fraction, tails_fraction

    class Analytics(Calculations):
        def predict_random(self, n):
            logging.info(f"Predicting random outcomes for {n} steps")
            predictions = []
            for _ in range(n):
                heads = randint(0, 1)
                tails = 1 - heads
                predictions.append([heads, tails])
            logging.info(f"Random predictions: {predictions}")
            return predictions

        def predict_last(self):
            logging.info("Predicting the last observation")
            if self.data:
                last_observation = self.data[-1]
                logging.info(f"Last observation: {last_observation}")
                return last_observation
            else:
                logging.info("No data available for last observation")
                return []

        def save_file(self, data, filename, extension='txt'):
            logging.info(f"Saving data to file {filename}.{extension}")
            full_filename = f"{filename}.{extension}"
            with open(full_filename, 'w') as file:
                file.write(data)
            logging.info(f"Data saved successfully to {full_filename}")

        def generate_report(self, heads_count, tails_count, heads_fraction, tails_fraction, random_predictions):
            logging.info("Generating report")
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
            logging.info(f"Report generated: {report}")
            return report
