import sys
from analytics import Research
import config

def main():
    if len(sys.argv) != 2:
        raise Exception("Usage: python make_report.py <path_to_file>")

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
        random_predictions = analytics.predict_random(config.NUM_OF_STEPS)
        print(random_predictions)

        last_prediction = analytics.predict_last()
        #print(last_prediction)

        # Генерация отчета
        report = analytics.generate_report(heads_count, tails_count, heads_fraction, tails_fraction, random_predictions)
        #print(report)

        # Сохранение отчета в файл
        analytics.save_file(report, "report", "txt")

    except (ValueError, FileNotFoundError, Exception) as e:
        print(e)

if __name__ == "__main__":
    main()
