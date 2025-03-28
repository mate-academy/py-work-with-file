import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as source:
        csv_reader = csv.reader(source)
        # next(csv_reader)

        for row in csv_reader:
            operation, amount = row
            amount = int(amount)
            if operation == "supply":
                supply_total += amount
            if operation == "buy":
                buy_total += amount

        result = supply_total - buy_total

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply_total}\n")
        report.write(f"buy,{buy_total}\n")
        report.write(f"result,{result}\n")
