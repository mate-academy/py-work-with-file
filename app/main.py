import csv
import os
from collections import defaultdict


def create_report(data_file_name: str, report_file_name: str) -> None:
    csv_file_path = os.path.join(os.path.dirname(__file__),
                                 "..", data_file_name)
    result_dict = defaultdict(int)

    with open(csv_file_path, "r") as csv_data:
        csvreader = csv.reader(csv_data)
        for row in csvreader:
            if len(row) == 2:
                operation, amount = row[0].strip(), row[1].strip()
                try:
                    result_dict[operation] += int(amount)
                except ValueError:
                    print(f"Invalid value: {amount}")

    result_dict["result"] = \
        (result_dict.get("supply", 0) - result_dict.get("buy", 0))

    report_file_path = os.path.join(os.path.dirname(__file__),
                                    "..", report_file_name)
    with open(report_file_path, "w", newline="") as report_file:
        writer = csv.writer(report_file)
        for key in ["supply", "buy", "result"]:
            writer.writerow([key, result_dict.get(key, 0)])
