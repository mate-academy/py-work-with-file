import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    # Initialize totals for 'supply' and 'buy'
    totals = {"supply": 0, "buy": 0}

    # Open and read the input CSV file
    with open(data_file_name, mode="r") as infile:
        reader = csv.reader(infile)
        for row in reader:
            # Ensure each row has the expected format (operation, amount)
            if len(row) != 2:
                continue  # Skip malformed rows

            operation, amount = row[0], row[1]
            try:
                # Convert amount to integer and update the corresponding total
                amount = int(amount)
                if operation in totals:
                    totals[operation] += amount
            except ValueError:
                # Skip rows where amount cannot be converted to an integer
                continue

    # Calculate the result: difference between supply and buy
    result = totals["supply"] - totals["buy"]

    # Open and write the output CSV file with newline='' to avoid extra lines
    with open(report_file_name, mode="w", newline='') as outfile:
        writer = csv.writer(outfile)
        # Write the totals and result to the file
        writer.writerow(["supply", totals["supply"]])
        writer.writerow(["buy", totals["buy"]])
        writer.writerow(["result", result])
