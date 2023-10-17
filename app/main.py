import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    buy = 0
    supply = 0
    with open(data_file_name, "r") as csv_file:
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            if row:
                operation, amount = row
                if operation == "supply":
                    supply += int(amount)
                elif operation == "buy":
                    buy += int(amount)

    with open(report_file_name, "w") as report_file:
        writer = csv.writer(report_file)
        writer.writerows([["supply", supply], ["buy", buy],
                          ["result", supply - buy]])
