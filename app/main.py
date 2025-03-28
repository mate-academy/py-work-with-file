import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_counter = 0
    buy_counter = 0

    with open(data_file_name, mode="r") as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            operation, amount = row[0], int(row[1])
            if operation == "supply":
                supply_counter += amount
            elif operation == "buy":
                buy_counter += amount

    result = supply_counter - buy_counter

    with open(report_file_name, "w", newline="") as report_file:
        csvwriter = csv.writer(report_file)
        csvwriter.writerow(["supply", supply_counter])
        csvwriter.writerow(["buy", buy_counter])
        csvwriter.writerow(["result", result])
