import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {"supply": 0, "buy": 0}

    with open(data_file_name, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:

            if not row:
                continue

            operation, amount = row
            amount = int(amount)

            if operation in totals:
                totals[operation] += amount

    result = totals["supply"] - totals["buy"]

    with open(report_file_name, mode="w", encoding="utf-8") as file:
        file.write(f"supply,{totals['supply']}\n")
        file.write(f"buy,{totals['buy']}\n")
        file.write(f"result,{result}\n")
