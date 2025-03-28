import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0
    with open(data_file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                operation_type, amount = row[0], int(row[1])
                if operation_type == "supply":
                    total_supply += amount
                if operation_type == "buy":
                    total_buy += amount

    result = total_supply - total_buy

    with open(report_file_name, "w", newline="") as report_file:
        csv_writer = csv.writer(report_file)
        supply = "supply", total_supply
        buy = "buy", total_buy
        result = "result", result
        csv_writer.writerow(supply)
        csv_writer.writerow(buy)
        csv_writer.writerow(result)
