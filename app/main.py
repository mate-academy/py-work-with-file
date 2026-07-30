import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, mode="r") as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            if not row:
                continue
            operation, amount = row
            amount = int(amount)
            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount
    result = supply - buy
    with open(report_file_name, mode="w", newline="") as report_file:
        writer = csv.writer(report_file)
        writer.writerow(["supply", supply])
        writer.writerow(["buy", buy])
        writer.writerow(["result", result])
