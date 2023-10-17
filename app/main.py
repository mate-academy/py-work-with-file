import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    # Read data from the input CSV file and calculate totals
    with open(data_file_name, "r") as data_file:
        csv_reader = csv.reader(data_file)
        for row in csv_reader:
            if row:
                operation, amount = row
                if operation == "supply":
                    supply_total += int(amount)
                elif operation == "buy":
                    buy_total += int(amount)

    # Calculate the result
    result = supply_total - buy_total

    # Write the report to the report file
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buy_total}\n")
        report_file.write(f"result,{result}\n")
