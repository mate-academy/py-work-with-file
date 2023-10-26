import csv


def create_report(data_file_name: str, report_file_name: str) -> None:

    supply = 0
    buy = 0
    with open(data_file_name, "r") as csv_data:
        csv_reader = csv.reader(csv_data)
        for row in csv_reader:
            if row[0] == "supply":
                supply += int(row[1])
            if row[0] == "buy":
                buy += int(row[1])
        result = supply - buy

    with open(report_file_name, "w", newline="") as csv_report:
        csv_writer = csv.writer(csv_report)

        csv_writer.writerow(["supply", supply])
        csv_writer.writerow(["buy", buy])
        csv_writer.writerow(["result", result])
