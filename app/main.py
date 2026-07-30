import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    # Dictionary to store totals for each operation type
    totals = {"supply": 0, "buy": 0}

    # Read data from the input CSV file
    with open(data_file_name, "r", newline="") as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            # Skip empty lines
            if not row:
                continue
            operation_type, amount = row
            # Update totals
            if operation_type in totals:
                totals[operation_type] += int(amount)

    # Calculate result
    result = totals["supply"] - totals["buy"]

    # Write report to the output file
    with open(report_file_name, "w", newline="") as report_file:
        writer = csv.writer(report_file)
        writer.writerow(["supply", str(totals["supply"])])
        writer.writerow(["buy", str(totals["buy"])])
        writer.writerow(["result", str(result)])
