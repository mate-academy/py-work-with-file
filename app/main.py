import csv


def create_report(data_file_name: str, report_file_name: str):
    buy = 0
    supply = 0
    with open(data_file_name, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            if row[0] == "buy":
                buy += int(row[1])
            elif row[0] == "supply":
                supply += int(row[1])
    result = supply - buy

    with open(report_file_name, "w") as csv_file_report:
        writer = csv.writer(csv_file_report, delimiter=",")
        writer.writerow(["supply", supply])
        writer.writerow(["buy", buy])
        writer.writerow(["result", result])
