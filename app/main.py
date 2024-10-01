import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, mode="r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if len(row) == 0:
                continue
            operation_type, amount = row[0], int(row[1])
            if operation_type == "supply":
                total_supply += amount
            elif operation_type == "buy":
                total_buy += amount

    result = total_supply - total_buy

    with open(report_file_name, mode="w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["supply", total_supply])
        csv_writer.writerow(["buy", total_buy])
        csv_writer.writerow(["result", result])
