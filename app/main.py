import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0
    with open(data_file_name, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                operation_type, amount = row
                if operation_type == "supply":
                    supply_total += int(amount)
                elif operation_type == "buy":
                    buy_total += int(amount)

    result = supply_total - buy_total

    with open(report_file_name, "w") as reportfile:
        reportfile.write(f'supply,{supply_total}\n')
        reportfile.write(f'buy,{buy_total}\n')
        reportfile.write(f'result,{result}\n')
