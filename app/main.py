import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, mode="r", newline="") as f1:
        reader = csv.reader(f1)
        for row in reader:
            if row:
                operation, amount = row
                if operation == "supply":
                    supply += int(amount)
                elif operation == "buy":
                    buy += int(amount)
    result = supply - buy
    with open(report_file_name, mode="w", newline="") as f2:
        writer = csv.writer(f2)
        writer.writerow(["supply", supply])
        writer.writerow(["buy", buy])
        writer.writerow(["result", result])
