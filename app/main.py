import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0
    with open(data_file_name, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if not row:
                continue
            operation_type, amount = row[0], int(row[1])
            if operation_type == "supply":
                total_supply += amount
            elif operation_type == "buy":
                total_buy += amount
    result = total_supply - total_buy
    with open(report_file_name, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["supply", total_supply])
        csvwriter.writerow(["buy", total_buy])
        csvwriter.writerow(["result", result])
