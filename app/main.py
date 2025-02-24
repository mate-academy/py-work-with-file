def create_report(
    data_file_name: str, report_file_name: str
) -> None:
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
        with open(data_file_name, "r") as data_file:
            for line in data_file:
                line = line.strip()
                if not line:
                    continue  # Пропускаємо порожні рядки

                parts = line.split(",")
                if len(parts) == 2:
                    operation_type, amount_str = parts
                    try:
                        amount = int(amount_str)
                        if operation_type == "supply":
                            supply_total += amount
                        elif operation_type == "buy":
                            buy_total += amount
                    except ValueError:
                        error_message = (
                            f"Помилка: Неможливо перетворити \"{amount_str}\""
                            f" на ціле число."
                        )
                        print(error_message)
                else:
                    error_message = (
                        f'Помилка: Неправильний формат рядка: "{line}"'
                    )
                    print(error_message)

        result = supply_total - buy_total

        with open(report_file_name, "w") as report_file:
            report_file.write(f"supply,{supply_total}\n")  # noqa: E231
            report_file.write(f"buy,{buy_total}\n")  # noqa: E231
            report_file.write(f"result,{result}\n")  # noqa: E231

    except FileNotFoundError:
        print(f'Помилка: Файл "{data_file_name}" не знайдено.')
    except Exception as e:
        print(f"Виникла помилка: {e}")


# Створення звітів для кожного файлу:
create_report("apples.csv", "report_apples.csv")
create_report("bananas.csv", "report_bananas.csv")
create_report("grapes.csv", "report_grapes.csv")
create_report("oranges.csv", "report_oranges.csv")

print("Звіти створено.")
