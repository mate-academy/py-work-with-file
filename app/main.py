import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    # Initializing supply and buy
    supply = 0
    buy = 0

    # Reading from csv file
    with open(data_file_name, "r") as data_file:
        csv_reader = csv.reader(data_file)
        for row in csv_reader:
            if len(row) != 0:  # Ignoring empty lines
                operation, amount = row
                if operation == "supply":
                    supply += int(amount)
                elif operation == "buy":
                    buy += int(amount)

    result = supply - buy

    # Writing to the report csv file
    with open(report_file_name, "w", newline="") as report_file:
        csv_writer = csv.writer(report_file)
        csv_writer.writerow(["supply", supply])
        csv_writer.writerow(["buy", buy])
        csv_writer.writerow(["result", result])
