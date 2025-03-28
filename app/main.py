import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    # Initialize counters for supply and buy
    supply_total = 0
    buy_total = 0

    # Read data from the input file
    with open(data_file_name, "r") as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            if row:  # Ensure we skip any empty lines
                operation, amount = row[0], int(row[1])
                if operation == "supply":
                    supply_total += amount
                elif operation == "buy":
                    buy_total += amount

    # Calculate the result
    result = supply_total - buy_total

    # Write the report to the output file
    with open(report_file_name, "w") as report_file:
        writer = csv.writer(report_file)
        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])
        writer.writerow(["result", result])
