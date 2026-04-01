import csv


def create_report(data_file_name: str, report_file_name: str) -> None:

    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as data_file:
        csv_reader = csv.reader(data_file)
        for row in csv_reader:
            if row:
                operation_type, amount = row
                if operation_type == "supply":
                    supply_total += int(amount)
                elif operation_type == "buy":
                    buy_total += int(amount)

    result = supply_total - buy_total

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buy_total}\n")
        report_file.write(f"result,{result}\n")
