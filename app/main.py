import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r", newline="") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if not row:
                continue
            if row[0] == "supply":
                supply_total += int(row[1])
            elif row[0] == "buy":
                buy_total += int(row[1])

    result = supply_total - buy_total

    with open(report_file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])
        writer.writerow(["result", result])
