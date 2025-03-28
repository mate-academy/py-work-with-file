import csv


def create_report(data_file_name: str, report_file_name: str) -> str:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, mode="r") as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            if len(row) == 0:
                continue

            operation_type, amount = row[0], int(row[1])

            if operation_type == "supply":
                supply_total += amount
            elif operation_type == "buy":
                buy_total += amount

    result = supply_total - buy_total

    with open(report_file_name, mode="w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["supply", supply_total])
        csv_writer.writerow(["buy", buy_total])
        csv_writer.writerow(["result", result])
