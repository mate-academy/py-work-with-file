import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    total = {}

    with open(data_file_name, "r", newline="") as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            if not row:
                continue
            operation_type, amount = row
            total[operation_type] = total.get(operation_type, 0) + int(amount)

        supply_total = total.get("supply", 0)
        buy_total = total.get("buy", 0)
        result = supply_total - buy_total

    with open(report_file_name, "w", newline="") as report_file:
        writer = csv.writer(report_file)
        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])
        writer.writerow(["result", result])
