import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {"supply": 0, "buy": 0}

    with open(data_file_name, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:
                continue
            operation_type = row[0]
            amount = int(row[1])
            if operation_type in totals:
                totals[operation_type] += amount

    result = totals["supply"] - totals["buy"]

    with open(report_file_name, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["supply", totals["supply"]])
        writer.writerow(["buy", totals["buy"]])
        writer.writerow(["result", result])
