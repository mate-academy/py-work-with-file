import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(
            data_file_name, mode="r", newline="", encoding="utf-8"
    ) as data_file:
        csv_reader = csv.reader(data_file)

        # Read rows from the CSV file
        for row in csv_reader:
            if len(row) != 2:
                continue  # Skip malformed rows
            operation, amount_str = row
            try:
                amount = int(amount_str)
            except ValueError:
                continue  # Skip rows with non-integer amounts

            # Accumulate totals based on operation type
            if operation == "supply":
                supply_total += amount
            elif operation == "buy":
                buy_total += amount

    # Calculate the result
    result = supply_total - buy_total

    # Write the report to the new CSV file
    with open(
            report_file_name, mode="w", newline="", encoding="utf-8"
    ) as report_file:
        csv_writer = csv.writer(report_file)
        csv_writer.writerow(["supply", supply_total])
        csv_writer.writerow(["buy", buy_total])
        csv_writer.writerow(["result", result])
