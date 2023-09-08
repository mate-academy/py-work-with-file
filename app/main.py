# write your code here
# app/main.py

import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as data_file:
        data_reader = csv.reader(data_file)

        for row in data_reader:
            if row:
                action, amount = row[0], int(row[1])
                if action == "supply":
                    supply_total += amount
                elif action == "buy":
                    buy_total += amount

    result = supply_total - buy_total

    # Write the report to the report_file_name with newline characters
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_total}\nbuy,"
                          f"{buy_total}\nresult,{result}\n")
