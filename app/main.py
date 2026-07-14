import csv
from typing import Dict


def create_report(data_file_name: str, report_file_name: str) -> None:
    """Створює звіт на основі даних з CSV файлу.

    Args:
        data_file_name: Шлях до вхідного CSV файлу.
        report_file_name: Шлях до вихідного CSV файлу для звіту.
    """
    operation_totals: Dict[str, int] = {"supply": 0, "buy": 0}

    with open(data_file_name, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:  # Пропускаємо порожні рядки
                continue
            operation, amount = row
            operation_totals[operation] = (
                operation_totals.get(operation, 0) + int(amount)
            )

    result = operation_totals["supply"] - operation_totals["buy"]

    with open(
        report_file_name, mode="w", encoding="utf-8", newline=""
    ) as file:
        writer = csv.writer(file)
        writer.writerow(["supply", operation_totals["supply"]])
        writer.writerow(["buy", operation_totals["buy"]])
        writer.writerow(["result", result])
