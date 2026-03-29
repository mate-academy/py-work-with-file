import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                operation, amount = row[0], row[1]
                try:
                    amount = int(amount)
                    if operation == "supply":
                        supply_total += amount
                    elif operation == "buy":
                        buy_total += amount
                except ValueError:
                    pass

    result = supply_total - buy_total

    with open(report_file_name, mode="w",
              encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])
        writer.writerow(["result", result])

# create_report("test.csv", "report.csv")
