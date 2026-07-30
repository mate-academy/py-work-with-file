import csv
from collections import defaultdict


def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = defaultdict(int)

    with open(data_file_name, "r") as data_file:
        csv_reader = csv.reader(data_file)
        for row in csv_reader:
            if row:
                operation_type, amount = row
                totals[operation_type] += int(amount)

    result = totals["supply"] - totals["buy"]

    with open(report_file_name, "w", newline="") as report_file:
        csv_writer = csv.writer(report_file)
        csv_writer.writerow(["supply", totals["supply"]])
        csv_writer.writerow(["buy", totals["buy"]])
        csv_writer.writerow(["result", result])
