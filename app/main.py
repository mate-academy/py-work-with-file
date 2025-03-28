import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    # Читання даних з CSV файлу
    with open(data_file_name, mode="r", newline="") as data_file:
        reader = csv.reader(data_file)

        for row in reader:
            if row:  # Якщо рядок не порожній
                operation, amount = row
                amount = int(amount)

                if operation == "supply":
                    supply += amount
                elif operation == "buy":
                    buy += amount

    # Обчислення результату
    result = supply - buy

    # Запис звіту в новий файл
    with open(report_file_name, mode="w", newline="") as report_file:
        writer = csv.writer(report_file)
        writer.writerow(["supply", supply])
        writer.writerow(["buy", buy])
        writer.writerow(["result", result])
