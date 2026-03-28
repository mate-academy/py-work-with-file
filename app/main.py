import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    # Read the input CSV file
    with open(data_file_name, "r") as data_file:
        csv_reader = csv.reader(data_file)
        for row in csv_reader:
            if len(row) == 2:  # Ensure the row has two fields
                operation_type, amount = row
                if operation_type == "supply":
                    supply_total += int(amount)
                elif operation_type == "buy":
                    buy_total += int(amount)

    # Calculate the result
    result = supply_total - buy_total

    # Write the report to the output CSV file
    with open(report_file_name, "w", newline="") as report_file:
        csv_writer = csv.writer(report_file)
        csv_writer.writerow(["supply", supply_total])
        csv_writer.writerow(["buy", buy_total])
        csv_writer.writerow(["result", result])
