
import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    # Initialize variables to store supply and buy amounts
    supply = 0
    buy = 0

    # Open the input file and read data
    with open(data_file_name, 'r') as data_file:
        reader = csv.reader(data_file)
        # Loop through each row of data and update supply and buy variables
        for row in reader:
            if row:  # Skip empty rows
                operation, amount = row
                if operation == 'supply':
                    supply += int(amount)
                elif operation == 'buy':
                    buy += int(amount)

    # Calculate the result
    result = supply - buy

    # Write the report to the output file
    with open(report_file_name, 'w') as report_file:
        writer = csv.writer(report_file)
        writer.writerow(['supply', supply])
        writer.writerow(['buy', buy])
        writer.writerow(['result', result])


