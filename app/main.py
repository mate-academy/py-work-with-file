import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_amount = 0
    buy_amount = 0

    with open(data_file_name, "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            operation_type, amount = row
            amount = int(amount)

            if operation_type == "supply":
                supply_amount += amount
            elif operation_type == "buy":
                buy_amount += amount

    result = supply_amount - buy_amount

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_amount}\n")
        report_file.write(f"buy,{buy_amount}\n")
        report_file.write(f"result,{result}\n")
