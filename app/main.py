from typing import Tuple


def _parse_line(line: str) -> Tuple[str, int]:
    """
    Parse a single CSV line of the form "operation,amount".

    Returns:
        tuple: (operation, amount).
    Raises:
        ValueError: If format is invalid or amount is not an integer.
    """
    line = line.strip()
    if not line:
        raise ValueError("Empty line")

    parts = [p.strip() for p in line.split(",")]
    if len(parts) != 2:
        raise ValueError(f"Invalid CSV row: {line!r}")

    operation, amount_str = parts
    try:
        amount = int(amount_str)
    except ValueError as exc:
        raise ValueError(
            f"Amount must be an integer: {amount_str!r}"
        ) from exc

    operation = operation.lower()
    if operation not in {"supply", "buy"}:
        raise ValueError(f"Unsupported operation: {operation!r}")

    return operation, amount


def create_report(data_file_name: str, report_file_name: str) -> None:
    """
    Read a CSV file with rows like:
        supply,30
        buy,10

    Sum amounts per operation and write a report:
        supply,<sum>
        buy,<sum>
        result,<supply - buy>

    Notes:
        - Ignores empty trailing lines.
        - Strips whitespace around fields.
        - Raises exceptions if rows are malformed.
    """
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r", encoding="utf-8") as file:
        for raw_line in file:
            line = raw_line.strip()
            if not line:
                continue
            operation, amount = _parse_line(line)
            if operation == "supply":
                supply_total += amount
            else:  # operation == "buy"
                buy_total += amount

    result = supply_total - buy_total

    with open(report_file_name, "w", encoding="utf-8") as file:
        file.write(f"supply,{supply_total}\n")
        file.write(f"buy,{buy_total}\n")
        file.write(f"result,{result}\n")
