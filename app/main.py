from __future__ import annotations

import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as data_file:
        reader = csv.reader(data_file)

        for row in reader:
            if not row:
                continue

            operation, amount = row

            if operation == "supply":
                supply += int(amount)
            elif operation == "buy":
                buy += int(amount)

    result = supply - buy

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{result}\n")
