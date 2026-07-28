import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {"supply": 0, "buy": 0}
    with open(data_file_name, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if not row or not row[0].strip():
                continue

            operation_type, amount = row[0], int(row[1])
            totals[operation_type] += amount

    result = totals["supply"] - totals["buy"]

    with open(report_file_name, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["supply", totals["supply"]])
        writer.writerow(["buy", totals["buy"]])
        writer.writerow(["result", result])
