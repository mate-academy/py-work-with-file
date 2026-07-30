import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total: int = 0
    buy_total: int = 0

    with open(data_file_name, mode="r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if not row:
                continue
            operation, amount_str = row
            amount = int(amount_str)
            if operation == "supply":
                supply_total += amount
            elif operation == "buy":
                buy_total += amount

    result: int = supply_total - buy_total

    with open(report_file_name, mode="w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])
        writer.writerow(["result", result])
