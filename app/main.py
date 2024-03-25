import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            operation, amount = row
            amount = int(amount)
            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount

    result = supply - buy

    report_data = [
        ["supply", supply],
        ["buy", buy],
        ["result", result],
    ]

    with open(report_file_name,
              "w",
              newline="",
              encoding="utf-8") as report_file:
        writer = csv.writer(report_file)
        for row in report_data:
            writer.writerow(row)
