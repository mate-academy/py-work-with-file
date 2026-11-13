import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    """Create a CSV report with supply, buy, and net result totals."""
    totals = {"supply": 0, "buy": 0}

    with open(data_file_name, newline="", encoding="utf-8") as data_file:
        for row in csv.reader(data_file):
            if not row:
                continue

            operation, amount = row
            totals[operation] += int(amount)

    with open(
        report_file_name, "w", newline="", encoding="utf-8"
    ) as report_file:
        writer = csv.writer(report_file, lineterminator="\n")
        writer.writerow(["supply", totals["supply"]])
        writer.writerow(["buy", totals["buy"]])
        writer.writerow(["result", totals["supply"] - totals["buy"]])
