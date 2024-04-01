import csv


def create_report(data_file_name: str, report_file_name: str) -> None:

    operation_totals = {"supply": 0, "buy": 0}

    with open(data_file_name, "r", newline="") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:

            if row:

                operation, amount = row[0], int(row[1])

                operation_totals[operation] += amount

    result = operation_totals["supply"] - operation_totals["buy"]

    with open(report_file_name, "w") as report_file:

        for operation, total_amount in operation_totals.items():
            report_file.write(f"{operation},{total_amount}\n")

        report_file.write(f"result,{result}\n")
