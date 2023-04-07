import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_amount = 0
    buy_amount = 0

    with open(data_file_name, newline="") as data_file:
        data_reader = csv.reader(data_file)
        for row in data_reader:
            if row:
                operation_type, amount = row
                if operation_type == "supply":
                    supply_amount += int(amount)
                elif operation_type == "buy":
                    buy_amount += int(amount)

    with open(report_file_name, "w", newline="") as report_file:
        report_writer = csv.writer(report_file)
        report_writer.writerow(["supply", supply_amount])
        report_writer.writerow(["buy", buy_amount])
        report_writer.writerow(["result", supply_amount - buy_amount])
