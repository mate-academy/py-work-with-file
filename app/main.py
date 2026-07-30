import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                operation, amount = row
                if operation == "supply":
                    supply_total += int(amount)
                elif operation == "buy":
                    buy_total += int(amount)

    result = supply_total - buy_total

    with open(report_file_name, "w") as report_file:
        writer = csv.writer(report_file)
        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])
        writer.writerow(["result", result])
