import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, mode="r", encoding="utf-8") as data_file:
        csv_reader = csv.reader(data_file)
        for row in csv_reader:
            if len(row) == 2:
                operation, amount = row
                try:
                    amount = int(amount)
                except ValueError:
                    continue

                if operation == "supply":
                    supply_total += amount
                elif operation == "buy":
                    buy_total += amount

    result = supply_total - buy_total

    with (open(report_file_name, mode="w", encoding="utf-8", newline="")
          as report_file):
        csv_writer = csv.writer(report_file)
        csv_writer.writerow(["supply", supply_total])
        csv_writer.writerow(["buy", buy_total])
        csv_writer.writerow(["result", result])
