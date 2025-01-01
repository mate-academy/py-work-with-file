import csv
import sys


def process_csv(input_file, output_file):
    supply_total = 0
    buy_total = 0

    # Чтение данных из входного файла
    with open(input_file, 'r') as infile:
        reader = csv.reader(infile)
        for row in reader:
            if len(row) < 2:  # Пропуск пустых строк
                continue
            operation, amount = row[0], int(row[1])

            if operation == 'supply':
                supply_total += amount
            elif operation == 'buy':
                buy_total += amount

    # Подсчет результата
    result = supply_total - buy_total

    # Запись отчета в новый файл
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['supply', supply_total])
        writer.writerow(['buy', buy_total])
        writer.writerow(['result', result])


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py input.csv output.csv")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    process_csv(input_file, output_file)
    print("Report generated successfully.")

