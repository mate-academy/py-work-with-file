import csv
from collections import defaultdict


def create_report(data_file_name: str, report_file_name: str) -> None:
    data = defaultdict(str)

    with open(data_file_name, "r") as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            key, value = row
            data[key] += value

    with open(report_file_name, "w", newline="") as report_file:
        writer = csv.writer(report_file)
        for key, value in data.items():
            writer.writerow([key, value])
