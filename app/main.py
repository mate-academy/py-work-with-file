import csv
from typing import Any


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total: int = 0
    buy_total: int = 0

    with open(data_file_name, mode="r", newline="") as file:
        reader: Any = csv.reader(file)

        for row in reader:
            if not row:  # Skip empty rows
                continue
            operation_type, amount = row
            amount = int(amount)

            if operation_type == "supply":
                supply_total += amount
            elif operation_type == "buy":
                buy_total += amount

    result: int = supply_total - buy_total

    with open(report_file_name, mode="w", newline="") as file:
        writer: Any = csv.writer(file)
        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])
        writer.writerow(["result", result])
