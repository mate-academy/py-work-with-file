import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:
                continue
            if row[0] == "supply":
                supply += int(row[1])
            elif row[0] == "buy":
                buy += int(row[1])
    result = supply - buy
    with open(report_file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["supply", supply])
        writer.writerow(["buy", buy])
        writer.writerow(["result", result])
