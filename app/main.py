import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_buy = 0
    total_supply = 0
    with open(data_file_name, "r") as csv_file:
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            if row:
                operation, amount = row
                if operation == "supply":
                    total_supply += int(amount)
                elif operation == "buy":
                    total_buy += int(amount)
    with open(report_file_name, "w", newline="") as report_file:
        writer = csv.writer(report_file)
        writer.writerows([["supply", total_supply], ["buy", total_buy],
                          ["result", total_supply - total_buy]])
