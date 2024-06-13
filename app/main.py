import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    operation_totals = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            operation_type, amount = row
            if operation_type in operation_totals:
                operation_totals[operation_type] += int(amount)

    result = operation_totals["supply"] - operation_totals["buy"]

    with open(report_file_name, "w") as reportfile:
        reportfile.write(
            f"supply,{operation_totals['supply']}\n"
            f"buy,{operation_totals['buy']}\n"
            f"result,{result}\n"
        )