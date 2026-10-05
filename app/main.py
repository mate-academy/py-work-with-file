import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {"supply": 0, "buy": 0}
    with open(data_file_name, newline="", encoding="utf-8") as data_file:
        for row in csv.reader(data_file):
            if row:
                operation, amount = row
                totals[operation] += int(amount)
    with open(report_file_name, "w", newline="", encoding="utf-8") as report:
        writer = csv.writer(report, lineterminator="\n")
        writer.writerow(["supply", totals["supply"]])
        writer.writerow(["buy", totals["buy"]])
        writer.writerow(["result", totals["supply"] - totals["buy"]])
