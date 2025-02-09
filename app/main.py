import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0
    with open(data_file_name, mode="r") as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            if not row or len(row) < 2:
                continue
            data_name, quantity = row[0].strip(), row[1].strip()
            try:
                quantity = int(quantity)
            except ValueError:
                continue
            if data_name == "buy":
                buy_total += quantity
            elif data_name == "supply":
                supply_total += quantity

    with open(report_file_name, mode="w", newline="") as report_file:
        writer = csv.writer(report_file)
        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])
