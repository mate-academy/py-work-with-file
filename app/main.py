import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as data_file:
        csv_reader = csv.reader(data_file)
        for row in csv_reader:
            if len(row) == 0:  # skip empty lines
                continue
            operation, amount = row
            if operation == "supply":
                supply += int(amount)
            elif operation == "buy":
                buy += int(amount)

    result = supply - buy

    with open(report_file_name, "w", newline="") as report_file:
        csv_writer = csv.writer(report_file)
        csv_writer.writerow(["supply", supply])
        csv_writer.writerow(["buy", buy])
        csv_writer.writerow(["result", result])
