import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_amount = 0
    buy_amount = 0
    with open(data_file_name, "r") as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            # Skip the last line if it's empty
            if not row:
                continue
            operation_type, amount = row[0], int(row[1])
            if operation_type == "supply":
                supply_amount += amount
            elif operation_type == "buy":
                buy_amount += amount
    result = supply_amount - buy_amount
    # Write the report to the output file
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply, {supply_amount}\n")
        report_file.write(f"buy, {buy_amount}\n")
        report_file.write(f"result, {result}\n")
