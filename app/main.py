import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as data_file:
        for row in csv.reader(data_file):
            if not row:
                continue
            operation, amount = row
            totals[operation.strip()] += int(amount)

    supply = totals["supply"]
    buy = totals["buy"]
    result = supply - buy

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{result}\n")
