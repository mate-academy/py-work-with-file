"""Market report generation from CSV data."""

import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    """
    Read market data from a CSV file, aggregate by operation type,
    and write a summary report to the output file.

    Input CSV format: operation_type,amount (one per line).
    Empty lines are skipped (e.g. trailing newline).
    Report: supply total, buy total, result (supply - buy).
    """
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r", newline="", encoding="utf-8") as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            if not row or len(row) < 2:
                continue
            op_type = row[0].strip()
            try:
                amount = int(row[1].strip())
            except ValueError:
                continue
            if op_type == "supply":
                supply_total += amount
            elif op_type == "buy":
                buy_total += amount

    result = supply_total - buy_total

    with open(
        report_file_name, "w", newline="", encoding="utf-8"
    ) as report_file:
        writer = csv.writer(report_file, lineterminator="\n")
        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])
        writer.writerow(["result", result])
