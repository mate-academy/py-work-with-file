import csv


def create_report(data_file_name: str, report_file_name: str):
    buy = 0
    supply = 0

    with open(data_file_name, "r") as f:
        csv_reader = csv.reader(f, delimiter=",")
        for row in csv_reader:
            if row[0] == "buy":
                buy += int(row[1])
            else:
                supply += int(row[1])

    with open(report_file_name, "w", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(["supply", supply])
        writer.writerow(["buy", buy])
        writer.writerow(["result", supply - buy])
