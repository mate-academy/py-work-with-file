import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)

        for row in reader:
            if not row:
                continue
            operation, amount = row
            amount = int(amount)
            if operation == "supply":
                total_supply += amount
            elif operation == "buy":
                total_buy += amount

    result = total_supply - total_buy

    with open(report_file_name, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["supply", total_supply])
        writer.writerow(["buy", total_buy])
        writer.writerow(["result", result])
