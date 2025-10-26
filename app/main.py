import csv
import os
os.chdir("/Users/admin/Documents/"
         "mate academy learning /"
         "github/py-work-with-file")


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data_file:
        data = csv.reader(data_file)
        for row in data:
            operation, amount = row[0], int(row[1])
            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{supply - buy}\n")
