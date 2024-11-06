import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    file_old = open(data_file_name, "r")
    reader = csv.reader(file_old)
    for row in reader:
        if not row:  # Skip empty lines
            continue

        operation_type, amount = row[0], int(row[1])
        if operation_type == "supply":
            supply_total += amount
        elif operation_type == "buy":
            buy_total += amount

    result = supply_total - buy_total

    new_file = open(report_file_name, mode="w", newline="")
    writer = csv.writer(new_file)
    writer.writerow(["supply", supply_total])
    writer.writerow(["buy", buy_total])
    writer.writerow(["result", result])
