import csv
import os
import sys


def create_report(data_file_name: str, report_file_name: str) -> None:
    """
    Зчитує CSV-файл, підраховує суми для операцій "supply" та "buy",
    обчислює різницю (результат) і записує звіт у новий CSV-файл.

    Аргументи:
        data_file_name (str): Ім'я CSV-файлу з вхідними даними.
        report_file_name (str): Ім'я CSV-файлу, куди буде записано звіт.
    """
    supply_total = 0
    buy_total = 0

    # Поточний файл — app/main.py
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Переходимо на один рівень вгору до кореневої директорії
    project_root = os.path.dirname(base_dir)
    # Формуємо шлях до директорії tests, де зараз знаходяться CSV-файли
    tests_dir = os.path.join(project_root, "tests")

    input_file_path = os.path.join(tests_dir, data_file_name)
    output_file_path = os.path.join(tests_dir, report_file_name)

    with open(input_file_path, "r", newline="") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            if not row or len(row) < 2:
                continue
            operation = row[0].strip()
            try:
                amount = int(row[1].strip())
            except ValueError:
                continue
            if operation == "supply":
                supply_total += amount
            elif operation == "buy":
                buy_total += amount

    result = supply_total - buy_total

    with open(output_file_path, "w", newline="") as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])
        writer.writerow(["result", result])


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "Використання: python -m app.main <data_file_name> "
            "<report_file_name>"
        )
        sys.exit(1)
    create_report(sys.argv[1], sys.argv[2])
