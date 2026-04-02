import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    operation_totals = {"supply": 0, "buy": 0}
    with open(data_file_name, "r", newline="") as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            if len(row) == 2:
                operation, amount = row
                if operation in operation_totals:
                    operation_totals[operation] += int(amount)
    result = operation_totals["supply"] - operation_totals["buy"]
    with open(report_file_name, "w", newline="") as report_file:
        writer = csv.writer(report_file)
        writer.writerow(["supply", operation_totals["supply"]])
        writer.writerow(["buy", operation_totals["buy"]])
        writer.writerow(["result", result])
