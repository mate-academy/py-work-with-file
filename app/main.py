import csv
from typing import Any


def create_report(data_file_name: str, report_file_name: str) -> Any:
    supply_count = 0
    buy_count = 0

    with open(data_file_name, "r", newline="") as data_file:
        reader = csv.reader(data_file)

        for row in reader:
            position, amount = row
            amount = int(amount)

            if position == "supply":
                supply_count += amount
            elif position == "buy":
                buy_count += amount

    result = supply_count - buy_count

    with open(report_file_name, "w", newline="") as report_file:
        writer = csv.writer(report_file)

        writer.writerow(["supply", supply_count])
        writer.writerow(["buy", buy_count])
        writer.writerow(["result", result])
