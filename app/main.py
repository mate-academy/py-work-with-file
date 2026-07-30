import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            if not row:
                continue

            operation_type, amount = row[0], int(row[1])

            if operation_type == "supply":
                supply_total += amount
            elif operation_type == "buy":
                buy_total += amount

    result = supply_total - buy_total

    with open(report_file_name, mode="w", newline="") as data_file:
        writer = csv.writer(data_file)
        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])
        writer.writerow(["result", result])
