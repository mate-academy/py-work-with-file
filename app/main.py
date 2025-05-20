import csv
import os


def process_csv(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    if not os.path.exists(data_file_name):
        raise FileNotFoundError(f"File {data_file_name} not found!")

    with open(data_file_name, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) < 2:
                continue

            try:
                operation, amount = row[0], int(row[1])
            except ValueError:
                continue

            if operation == "supply":
                supply_total += amount
            elif operation == "buy":
                buy_total += amount

    result = supply_total - buy_total

    report_dir = os.path.dirname(report_file_name)
    if report_dir and not os.path.exists(report_dir):
        os.makedirs(report_dir)

    with open(report_file_name, mode="w", newline="") as reportfile:
        writer = csv.writer(reportfile)
        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])
        writer.writerow(["result", result])
