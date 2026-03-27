import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_amounts = {}
    buy_amounts = {}

    with open(data_file_name, "r") as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if len(row) >= 2:
                operation_type, amount = row[0], int(row[1])
                if operation_type == "supply":
                    supply_amounts[operation_type] = (
                        supply_amounts.get(operation_type, 0) + amount
                    )
                elif operation_type == "buy":
                    buy_amounts[operation_type] = (
                        buy_amounts.get(operation_type, 0) + amount
                    )

    total_supply = sum(supply_amounts.values())
    total_buy = sum(buy_amounts.values())

    result = total_supply - total_buy

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{result}\n")
