import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    # Dictionary to store the total amounts for each operation type
    operation_totals = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Check if the row is not empty
                operation_type, amount = row
                if operation_type in operation_totals:
                    operation_totals[operation_type] += int(amount)

    supply_total = operation_totals["supply"]
    buy_total = operation_totals["buy"]
    result = supply_total - buy_total

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buy_total}\n")
        report_file.write(f"result,{result}\n")
