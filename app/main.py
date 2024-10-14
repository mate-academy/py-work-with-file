import csv
from collections import defaultdict


def create_report(data_file_name: str, report_file_name: str) -> None:
    # Dictionary to store totals for each operation type
    totals = defaultdict(int)

    # Read the data from the CSV file
    with open(data_file_name, mode="r", newline="") as data_file:
        csv_reader = csv.reader(data_file)

        # Process each row in the CSV
        for row in csv_reader:
            # Skip empty rows
            if not row:
                continue
            if len(row) != 2:  # Ensure there are two columns
                continue
            operation_type, amount = row[0].strip(), row[1].strip()
            # Strip whitespace
            try:
                # Convert the amount to an integer and add it
                # to the respective operation type total
                amount = int(amount)
                totals[operation_type] += amount
            except ValueError:
                print(f"Invalid amount '{amount}' for"
                      f" operation '{operation_type}'. Skipping.")

    # Calculate result
    result = totals["supply"] - totals["buy"]

    # Write the report to the output file
    with open(report_file_name, mode="w", newline="") as report_file:
        csv_writer = csv.writer(report_file)

        # Write totals for each operation type to the report
        for operation_type in ["supply", "buy"]:
            csv_writer.writerow([operation_type, totals[operation_type]])

        # Write the result
        csv_writer.writerow(["result", result])
