import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {"buy": 0, "supply": 0}
    with open(data_file_name, "r", newline="") as data_file:
        data = csv.reader(data_file, delimiter=",")
        for operation, value in data:
            report[operation] += int(value)
    with open(report_file_name, "w", newline="") as report_file:
        report_writer = csv.writer(report_file, delimiter=",")
        report = [
            ["supply", report["supply"]],
            ["buy", report["buy"]],
            ["result", report["supply"] - report["buy"]]
        ]
        report_writer.writerows(report)
