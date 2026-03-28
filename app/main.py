from __future__ import annotations

import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    """
    Read a CSV of operations and amounts, aggregate totals,
    and write a summary report.

    Input CSV expectations:
      - Two columns per row: operation, amount
      - operation in {"supply", "buy"} (case-insensitive)
      - amount is an integer
      - blank/empty lines are ignored
      - malformed rows are skipped gracefully

    Output file format:
        supply,<sum_of_supply>\n
        buy,<sum_of_buy>\n
        result,<supply_minus_buy>\n
    """
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r", encoding="utf-8", newline="") as src:
        reader = csv.reader(src)
        for row in reader:
            # Ignore completely empty lines
            if not row or all(cell.strip() == "" for cell in row):
                continue

            # Expect exactly two columns
            if len(row) != 2:
                # Skip malformed rows silently per spec's tolerance
                continue

            op_raw, amount_raw = row
            op = op_raw.strip().lower()

            # Only process recognized operations
            if op not in {"supply", "buy"}:
                continue

            # Coerce amount to int; skip if not valid
            try:
                amount = int(amount_raw.strip())
            except ValueError:
                continue

            if op == "supply":
                supply_total += amount
            else:  # op == "buy"
                buy_total += amount

    result = supply_total - buy_total

    # Write exactly in required format (with trailing newlines)
    with open(report_file_name, "w", encoding="utf-8", newline="") as dst:
        dst.write(f"supply,{supply_total}\n")
        dst.write(f"buy,{buy_total}\n")
        dst.write(f"result,{result}\n")
