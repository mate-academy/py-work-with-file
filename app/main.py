import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, newline="") as data_file:
        for row in csv.reader(data_file):
            if not row:
                continue

            operation, amount = row
            if operation == "supply":
                supply += int(amount)
            elif operation == "buy":
                buy += int(amount)

    with open(report_file_name, "w", newline="") as report_file:
        writer = csv.writer(report_file, lineterminator="\n")
        writer.writerows(
            [
                ("supply", supply),
                ("buy", buy),
                ("result", supply - buy),
            ]
        )
