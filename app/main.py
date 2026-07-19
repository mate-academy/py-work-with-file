import os


def create_report(data_file_name: str, report_file_name: str) -> None:
    # 1. Визначаємо, де лежить цей скрипт (main.py)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(current_dir)

    # 2. Якщо вхідний файл (наприклад, apples.csv) не знайдено там, 
    # де запущено термінал, шукаємо його в корені проєкту
    resolved_data_file = data_file_name
    if not os.path.exists(resolved_data_file):
        resolved_data_file = os.path.join(root_dir, data_file_name)

    supply_total = 0
    buy_total = 0

    # Читаємо файл
    with open(resolved_data_file, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            operation, amount = line.split(",")
            amount = int(amount)

            if operation == "supply":
                supply_total += amount
            elif operation == "buy":
                buy_total += amount

    result = supply_total - buy_total

    # 3. Записуємо звіт СУВОРО за тим шляхом, який вимагає тест!
    # Тест хоче бачити його в робочій директорії, тому не змінюємо report_file_name.
    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply_total}\n")
        report.write(f"buy,{buy_total}\n")
        report.write(f"result,{result}\n")


if __name__ == "__main__":
    create_report("oranges.csv", "report.csv")
