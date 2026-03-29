import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    """
    Створює звіт на основі даних з CSV файлу.

    Args:
        data_file_name: Назва вхідного CSV файлу.
        report_file_name: Назва файлу звіту,
        в який потрібно записати результат.
    """
    supply_total = 0
    buy_total = 0

    try:
        with open(data_file_name, "r", newline="") as data_file:
            reader = csv.reader(data_file)

            for row in reader:
                if len(row) != 2:
                    continue  # Пропускаємо некоректні рядки

                operation_type, amount_str = row

                try:
                    amount = int(amount_str)
                    if operation_type == "supply":
                        supply_total += amount
                    elif operation_type == "buy":
                        buy_total += amount
                except ValueError:
                    continue  # Пропускаємо некоректні значення

        result = supply_total - buy_total

        with open(report_file_name, "w", newline="") as report_file:
            writer = csv.writer(report_file)
            writer.writerow(["supply", supply_total])
            writer.writerow(["buy", buy_total])
            writer.writerow(["result", result])

    except FileNotFoundError:
        print(f'Помилка: Файл "{data_file_name}" не знайдено.')
    except Exception as e:
        print(f"Виникла помилка: {e}")


# Виклик функції з тестовими файлами
create_report("apples.csv", "report_apples.csv")
create_report("bananas.csv", "report_bananas.csv")
create_report("grapes.csv", "report_grapes.csv")
create_report("oranges.csv", "report_oranges.csv")

print("Звіти створено.")
