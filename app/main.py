import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0
    with open(data_file_name, mode="r", newline="") as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            if row:
                action, value = row
                value = int(value)
            if action == "supply":
                supply_total += value
            elif action == "buy":
                buy_total += value
    result = supply_total - buy_total

    with open(report_file_name, mode="w", newline="") as report_file:
        writer = csv.writer(report_file)
        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])
        writer.writerow(["result", result])
