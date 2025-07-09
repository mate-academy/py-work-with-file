def create_report(data_file_name: str, report_file_name: str) -> None:
    """
    Створює звіт на основі даних з CSV файлу.

    Args:
        data_file_name (str): Назва файлу з вхідними даними
        report_file_name (str): Назва файлу для збереження звіту
    """
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            if len(parts) >= 2:
                operation_type = parts[0].strip()
                amount = int(parts[1].strip())

                if operation_type == "supply":
                    total_supply += amount
                elif operation_type == "buy":
                    total_buy += amount

    result = total_supply - total_buy

    with open(report_file_name, "w", encoding="utf-8") as file:
        file.write(f"supply,{total_supply}\n")
        file.write(f"buy,{total_buy}\n")
        file.write(f"result,{result}\n")


if __name__ == "__main__":
    test_data = """supply,30
buy,10
buy,13
supply,17
buy,10
"""

    with open("test_data.csv", "w", encoding="utf-8") as f:
        f.write(test_data)

    create_report("test_data.csv", "report.csv")

    print("Звіт створено! Вміст файлу report.csv:")
    with open("report.csv", "r", encoding="utf-8") as f:
        print(f.read())
