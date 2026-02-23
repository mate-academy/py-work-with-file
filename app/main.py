import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    data_file = open(data_file_name, mode="r", newline="")
    reader = csv.reader(data_file)

    for row in reader:
        operation_type = row[0]
        amount = int(row[1])

        if operation_type == "supply":
            supply_total += amount
        if operation_type == "buy":
            buy_total += amount

    data_file.close()

    report_file = open(report_file_name, mode="w", newline="")
    writer = csv.writer(report_file)

    writer.writerow(["supply", supply_total])
    writer.writerow(["buy", buy_total])
    writer.writerow(["result", supply_total - buy_total])

    report_file.close()
