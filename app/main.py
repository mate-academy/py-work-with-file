import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, newline="") as csvfile:
        csvreader = csv.reader(csvfile)

        for row in csvreader:
            if len(row) == 0:
                continue
            operation_type, amount = row
            amount = int(amount)

            if operation_type == "supply":
                supply_total += amount
            elif operation_type == "buy":
                buy_total += amount
    result = supply_total - buy_total
    with open(report_file_name, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["supply", supply_total])
        csvwriter.writerow(["buy", buy_total])
        csvwriter.writerow(["result", result])
