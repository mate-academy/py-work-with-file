import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    # Read the CSV file and calculate totals
    with open(data_file_name, mode="r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:  # Ensure valid data
                operation, amount = row
                try:
                    amount = int(amount)
                    if operation == "supply":
                        supply_total += amount
                    elif operation == "buy":
                        buy_total += amount
                except ValueError:
                    continue  # Skip invalid rows

    result = supply_total - buy_total

    # Write the report to a new CSV file
    with open(report_file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])
        writer.writerow(["result", result])

# Example usage:
# create_report("input.csv", "report.csv")
