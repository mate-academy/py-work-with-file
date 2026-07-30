import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    try:
        with open(data_file_name, "r", newline="") as data_file:
            reader = csv.reader(data_file)
            for row in reader:
                if row:
                    operation_type, amount_str = row
                    try:
                        amount = int(amount_str)
                        if operation_type == "supply":
                            supply_total += amount
                        elif operation_type == "buy":
                            buy_total += amount
                    except ValueError:
                        print(f"Помилка: Не вдалося перетворити суму"
                              f"{amount_str} у ціле число в рядку: {row}")
    except FileNotFoundError:
        print(f"Помилка: Файл {data_file_name} не знайдено.")
        return
    except Exception as e:
        print(f"Виникла непередбачена помилка під час читання файлу: {e}")
        return

    result = supply_total - buy_total

    try:
        with open(report_file_name, "w", newline="") as report_file:
            writer = csv.writer(report_file)
            writer.writerow(["supply", supply_total])
            writer.writerow(["buy", buy_total])
            writer.writerow(["result", result])
        print(f"Звіт успішно створено та записано у файл {report_file_name}.")
    except Exception as e:
        print(f"Виникла помилка під час запису звіту у файл: {e}")
