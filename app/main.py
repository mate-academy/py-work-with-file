import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_amount = 0
    buy_amount = 0

    with open(data_file_name, "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            info, amount = row
            amount = int(amount)
            if info == "supply":
                supply_amount += amount
            elif info == "buy":
                buy_amount += amount

    result = supply_amount - buy_amount

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{str(supply_amount)}\n")
        report_file.write(f"buy,{str(buy_amount)}\n")
        report_file.write(f"result,{str(result)}\n")
