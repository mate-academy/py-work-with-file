import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row and len(row) == 2:
                operation, amount = row
                amount = int(amount)
                if operation == "supply":
                    supply += amount
                elif operation == "buy":
                    buy += amount
    result = [("supply", supply), ("buy", buy), ("result", supply - buy)]
    with open(report_file_name, "w", newline="") as file_report:
        writer = csv.writer(file_report)
        writer.writerows(result)
