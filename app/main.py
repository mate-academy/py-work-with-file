import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0
    with open(data_file_name, mode="r") as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            if len(row) == 0:
                continue
            operation, amount = row[0], int(row[1])
            if operation == "supply":
                supply_total += amount
            elif operation == "buy":
                buy_total += amount

    result = supply_total - buy_total
    with open(report_file_name, mode="w", newline="") as report_file:
        writer = csv.writer(report_file)
        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])
        writer.writerow(["result", result])
