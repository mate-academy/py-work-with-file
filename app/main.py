import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        reader = csv.reader(data_file)
        total_buy = 0
        total_supply = 0
        for row in reader:
            if not row:
                continue
            operation_type,amount = row[0], int(row[1])
            if operation_type == "supply":
                total_supply += amount
            if operation_type == "buy":
                total_buy += amount

        result = total_supply - total_buy

    with open(report_file_name, "w", newline="") as report_file:
        writer = csv.writer(report_file)
        writer.writerow(["supply",total_supply])
        writer.writerow(["buy", total_buy])
        writer.writerow(["result", result])
