import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    try:
        """
        Open the input CSV file and read its contents.
        """
        # Initialize dictionaries to store total amounts
        # for each operation type
        operation_totals = {"supply": 0, "buy": 0}

        # Open the input CSV file and read its contents
        with open(data_file_name, mode="r") as data_file:
            csv_reader = csv.reader(data_file)

            """
            Iterate over each row in the CSV file
            """
            for row in csv_reader:
                # Check if the row is not empty
                if row:
                    # Extract operation type and amount from the row
                    operation, amount = row

                    # Update the total amount for the corresponding
                    # operation type
                    operation_totals[operation] += int(amount)

        # Calculate the result (supply - buy)
        result = operation_totals["supply"] - operation_totals["buy"]

        """
        Write the report to the output file
        """
        with open(report_file_name, mode="w") as report_file:
            report_file.write(f"supply,{operation_totals['supply']}\n")
            report_file.write(f"buy,{operation_totals['buy']}\n")
            report_file.write(f"result,{result}\n")

        print("Report created successfully.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
