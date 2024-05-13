import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    operation_totals = {"supply": 0, "buy": 0}

    try:
        with open(data_file_name, newline="") as data_file:
            reader = csv.reader(data_file)
            for row in reader:
                if row:
                    operation, amount = row
                    if operation in operation_totals:
                        operation_totals[operation] += int(amount)

        # Calculate the result
        result = operation_totals["supply"] - operation_totals["buy"]

        # Write the report to the output file
        with open(report_file_name, "w") as report_file:
            report_file.write(f"supply,{operation_totals["supply"]}\n")
            report_file.write(f"buy,{operation_totals["buy"]}\n")
            report_file.write(f"result,{result}\n")

        print("Report created successfully.")
    except FileNotFoundError:
        print("Error: Input file not found.")
