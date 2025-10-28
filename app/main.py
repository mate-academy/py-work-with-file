def create_report(data_file_name: str, report_file_name: str) -> None:
    """Read market data from CSV and create a summary report."""
    supply_total = 0
    buy_total = 0

    # Read data from CSV file
    with open(data_file_name, "r", encoding="utf-8") as data_file:
        for line in data_file:
            line = line.strip()
            if not line:
                continue

            operation, amount = line.split(",")
            amount = int(amount)

            if operation == "supply":
                supply_total += amount
            elif operation == "buy":
                buy_total += amount

    # Calculate result
    result = supply_total - buy_total

    # Write report to file
    with open(report_file_name, "w", encoding="utf-8") as report_file:
        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buy_total}\n")
        report_file.write(f"result,{result}\n")