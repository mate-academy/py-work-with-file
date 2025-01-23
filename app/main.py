import csv


def process_csv_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    # Read the data from the input file
    with open(data_file_name, 'r') as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            if len(row) == 0:  # Skip empty lines
                continue
            operation_type, amount = row
            amount = int(amount)
            if operation_type == "supply":
                supply_total += amount
            elif operation_type == "buy":
                buy_total += amount

    # Calculate result
    result = supply_total - buy_total

    # Write the report to the output file
    with open(report_file_name, 'w', newline='') as report_file:
        writer = csv.writer(report_file)
        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])
        writer.writerow(["result", result])



