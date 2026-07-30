import csv


def create_report(data_file_name: str, report_file_name: str) -> str:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            if not row:
                continue
            if row and len(row) == 2:
                operation, amount = row
                amount = int(amount)
            if operation == "supply":
                supply_total += amount
            elif operation == "buy":
                buy_total += amount

    result = supply_total - buy_total

    with open(report_file_name, "w") as report_file:
        writer = csv.writer(report_file)
        writer.writerows(
            [["supply", supply_total], ["buy", buy_total], ["result", result]]
        )
