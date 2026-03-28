def create_report(data_file_name: str, report_file_name: str) -> None:
    """
    Reads a CSV file of market operations, calculates totals,
    and writes a summary report to another file.
    """
    supply_total = 0
    buy_total = 0

    try:
        with open(data_file_name, "r") as data_file:
            for line in data_file:
                if not line.strip():
                    continue

                parts = line.strip().split(",")
                if len(parts) == 2:
                    operation_type = parts[0]
                    amount_str = parts[1]

                    if operation_type == "supply":
                        supply_total += int(amount_str)
                    elif operation_type == "buy":
                        buy_total += int(amount_str)

    except FileNotFoundError:
        return

    result = supply_total - buy_total

    report_content = (
        f"supply,{supply_total}\n"
        f"buy,{buy_total}\n"
        f"result,{result}\n"
    )

    with open(report_file_name, "w") as report_file:
        report_file.write(report_content)
