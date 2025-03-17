import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    # Читання даних з CSV файлу
    with open(data_file_name, mode="r") as infile:
        reader = csv.reader(infile)

        # Обробка кожного рядка
        for row in reader:
            if len(row) == 2:  # Переконатися, що рядок містить два елементи
                operation_type = row[0].strip()
                amount = row[1].strip()

                # Обробка суми в залежності від типу операції
                if operation_type == "supply":
                    supply_total += int(amount)
                elif operation_type == "buy":
                    buy_total += int(amount)

    result = supply_total - buy_total  # Обчислення результату

    # Запис звіту у новий CSV файл
    with open(report_file_name, mode="w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])
        writer.writerow(["result", result])
