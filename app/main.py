import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, newline="") as data_file:
        for row in csv.reader(data_file):
            if not row:
                continue
            operation, amount = row
            if operation == "supply":
                supply_total += int(amount)
            elif operation == "buy":
                buy_total += int(amount)

    with open(report_file_name, "w", newline="") as report_file:
        writer = csv.writer(report_file, lineterminator="\n")
        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])
        writer.writerow(["result", supply_total - buy_total])
