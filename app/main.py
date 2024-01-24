import csv
from typing import Callable


def create_report(
        data_file_name: Callable,
        report_file_name: Callable
) -> None:

    supply_total = 0
    buy_total = 0

    with open(data_file_name, mode="r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                operation, amount = row[0], int(row[1])
                if operation == "supply":
                    supply_total += amount
                elif operation == "buy":
                    buy_total += amount

    result = supply_total - buy_total

    with open(report_file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])
        writer.writerow(["result", result])
