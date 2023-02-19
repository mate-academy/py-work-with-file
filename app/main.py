import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            if not row:
                continue
            operation_type, amount = row
            amount = int(amount)
            if operation_type == "supply":
                supply_total += amount
            elif operation_type == "buy":
                buy_total += amount

    result = supply_total - buy_total
    report = f"supply,{supply_total}\nbuy,{buy_total}\nresult,{result}\n"

    with open(report_file_name, "w") as report_file:
        report_file.write(report)
