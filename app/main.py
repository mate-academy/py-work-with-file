import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:
                continue
            operation, amount = row[0], int(row[1])
            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount
    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\n")
        report.write(f"buy,{buy}\n")
        report.write(f"result,{supply - buy}\n")
