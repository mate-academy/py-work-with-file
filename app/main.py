import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_sup = 0
    total_buy = 0

    file_name = open(data_file_name, "r")
    reader = csv.reader(file_name)
    for row in reader:
        if len(row) != 2:
            continue

        operation_type, amount = row
        amount = int(amount)

        if operation_type == "buy":
            total_buy += amount

        if operation_type == "supply":
            total_sup += amount

    result = total_sup - total_buy

    report = open(report_file_name, "w", newline="")
    writer = csv.writer(report)
    writer.writerow(["supply", total_sup])
    writer.writerow(["buy", total_buy])
    writer.writerow(["result", result])
