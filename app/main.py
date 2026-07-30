import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as data_file:
        csv_reader = csv.reader(data_file)

        for row in csv_reader:
            if row:
                operation_type, amount = row[0], int(row[1])
                if operation_type == "supply":
                    total_supply += amount
                elif operation_type == "buy":
                    total_buy += amount

    result = total_supply - total_buy

    with open(report_file_name, "w", newline="") as report_file:
        csv_writer = csv.writer(report_file)
        csv_writer.writerow(["supply", total_supply])
        csv_writer.writerow(["buy", total_buy])
        csv_writer.writerow(["result", result])
