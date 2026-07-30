import csv


def create_report(data_file_name: any, report_file_name: any) -> None:
    # Initialize variables to store total supply and buy
    total_supply = 0
    total_buy = 0

    # Read data from the CSV file
    with open(data_file_name, "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row:
                operation_type, amount = row[0], int(row[1])
                if operation_type == "supply":
                    total_supply += amount
                elif operation_type == "buy":
                    total_buy += amount

    # Calculate the result
    result = total_supply - total_buy

    # Write the report to the output file
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{result}\n")
