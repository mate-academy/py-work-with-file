import csv


def create_report(data_file_name: str, report_file_name: str) -> int:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 2:  # Only process rows with exactly 2 columns
                operation_type, amount = row
                amount = int(amount)
                if operation_type == "supply":
                    total_supply += amount
                elif operation_type == "buy":
                    total_buy += amount

    result = total_supply - total_buy

    with open(report_file_name, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["supply", total_supply])
        writer.writerow(["buy", total_buy])
        writer.writerow(["result", result])
