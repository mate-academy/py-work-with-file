import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r", newline="") as file:
        reader = csv.reader(file)

        for line in reader:
            if not line:
                continue
            operation, amount = line
            amount = int(amount)
            if operation == "supply":
                total_supply += amount
            elif operation == "buy":
                total_buy += amount

    result = total_supply - total_buy

    with open(report_file_name, "a", newline="") as file2:
        writer = csv.writer(file2)
        writer.writerow(["supply", total_supply])
        writer.writerow(["buy", total_buy])
        writer.writerow(["result", result])
