import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    operations = {}

    with open(data_file_name, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                operation_type, amount = row
                amount = int(amount)
                if operation_type in operations:
                    operations[operation_type] += amount
                else:
                    operations[operation_type] = amount

    with open(report_file_name, "w") as report_file:
        supply_total = operations.get("supply", 0)
        buy_total = operations.get("buy", 0)
        result = supply_total - buy_total

        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buy_total}\n")
        report_file.write(f"result,{result}\n")
