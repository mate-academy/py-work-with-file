import csv

def main(data_file_name: str, report_file_name: str) -> None:
    """Читает CSV файл, обрабатывает операции поставки и покупки и записывает отчет."""
    supply_total: int = 0
    buy_total: int = 0

    # Чтение данных из CSV файла
    with open(data_file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:  # Убедитесь, что строка содержит два элемента
                operation, amount = row
                if operation == "supply":
                    supply_total += int(amount)
                elif operation == "buy":
                    buy_total += int(amount)

    # Вычисление результата
    result: int = supply_total - buy_total

    # Запись отчета в новый файл
    with open(report_file_name, "w", encoding="utf-8") as file:
        file.write(f"supply,{supply_total}\n")
        file.write(f"buy,{buy_total}\n")
        file.write(f"result,{result}\n")
