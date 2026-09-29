import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {"supply": 0, "buy": 0}

    with open(data_file_name, "r", newline="") as data_file:
        for row in csv.reader(data_file):
            if not row:
                continue
            operation_type, amount = row
            totals[operation_type] += int(amount)

    with open(report_file_name, "w", newline="") as report_file:
        writer = csv.writer(report_file, lineterminator="\n")
        writer.writerow(["supply", totals["supply"]])
        writer.writerow(["buy", totals["buy"]])
        writer.writerow(["result", totals["supply"] - totals["buy"]])
