import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {
        "supply": 0,
        "buy": 0
    }
    with open(data_file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:
                continue

            operation_type = row[0].strip()
            amount = row[1].strip()

            try:
                amount = int(amount)
            except ValueError:
                continue

            if operation_type in data:
                data[operation_type] += amount

    supply_total = data["supply"]
    buy_total = data["buy"]
    result = supply_total - buy_total

    with open(report_file_name, "w", newline="") as file2:
        writer = csv.writer(file2)
        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])
        writer.writerow(["result", result])
