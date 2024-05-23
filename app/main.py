import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    # Read data from the CSV file
    with open(data_file_name, mode="r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # Check if the row is not empty
                operation_type, amount = row[0], int(row[1])
                if operation_type == "supply":
                    total_supply += amount
                elif operation_type == "buy":
                    total_buy += amount

    # Calculate the result
    result = total_supply - total_buy

    # Write the report to a new CSV file
    with open(report_file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["supply", total_supply])
        writer.writerow(["buy", total_buy])
        writer.writerow(["result", result])
