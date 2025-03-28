import csv


def create_report(data_file_name: str, report_file_name: str) -> str:
    supply_value = 0
    buy_value = 0
    with open(data_file_name, "r") as data:
        reader = csv.reader(data)
        for operation, value in reader:
            if operation == "supply":
                supply_value += int(value)
            if operation == "buy":
                buy_value += int(value)

    with open(report_file_name, "w", newline="") as report:
        writer = csv.writer(report)
        writer.writerow(["supply", supply_value])
        writer.writerow(["buy", buy_value])
        writer.writerow(["result", supply_value - buy_value])
