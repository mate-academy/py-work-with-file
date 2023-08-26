import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    # Initialize counters for supply and buy
    supply_total = 0
    buy_total = 0

    # Open the input CSV file and calculate totals
    with open(data_file_name, "r", newline="") as data_file:
        csv_reader = csv.reader(data_file)
        for row in csv_reader:
            if len(row) == 2:
                operation, amount = row
                if operation == "supply":
                    supply_total += int(amount)
                elif operation == "buy":
                    buy_total += int(amount)

    # Calculate the result
    result = supply_total - buy_total

    # Write the report to the output file
    with open(report_file_name, "w", newline="") as report_file:
        csv_writer = csv.writer(report_file)
        csv_writer.writerow(["supply", str(supply_total)])
        csv_writer.writerow(["buy", str(buy_total)])
        csv_writer.writerow(["result", str(result)])
