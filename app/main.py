import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r", newline="") as infile:
        csv_reader = csv.reader(infile)
        for row in csv_reader:
            if row:
                operation, amount = row
                amount = int(amount)
                if operation == "supply":
                    supply += amount
                elif operation == "buy":
                    buy += amount

    result = supply - buy

    with open(report_file_name, "w", newline="") as outfile:
        csv_writer = csv.writer(outfile)

        csv_writer.writerow(["supply", supply])
        csv_writer.writerow(["buy", buy])
        csv_writer.writerow(["result", result])
