import csv
from typing import Any


def create_report(data_file_name: str, report_file_name: str) -> Any:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:
                continue
            operation_type, amount = row
            amount = int(amount)
            if operation_type == "supply":
                total_supply += amount
            elif operation_type == "buy":
                total_buy += amount

    result = total_supply - total_buy

    with open(report_file_name, "w") as report_file:
        report_file.write("supply,"f"{total_supply}\n")
        report_file.write("buy,"f"{total_buy}\n")
        report_file.write("result,"f"{result}\n")
