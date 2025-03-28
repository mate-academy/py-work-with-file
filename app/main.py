import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:
                operation_type, amount = row
                if operation_type in totals:
                    totals[operation_type] += int(amount)

    result = totals["supply"] - totals["buy"]

    with open(report_file_name, "w") as reportfile:
        reportfile.write(f"supply,{totals['supply']}\n")
        reportfile.write(f"buy,{totals['buy']}\n")
        reportfile.write(f"result,{result}\n")
