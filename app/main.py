import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r", newline="") as csvfile:
        csvreader = csv.reader(csvfile)
        supply = 0
        buy = 0
        for row in csvreader:
            if row[0] == "supply":
                supply += int(row[1])
            elif row[0] == "buy":
                buy += int(row[1])
    with open(report_file_name, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["supply", supply])
        csvwriter.writerow(["buy", buy])
        csvwriter.writerow(["result", supply - buy])
