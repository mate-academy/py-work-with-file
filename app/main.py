def create_report(data_file_name: str, report_file_name: str) -> None:

    supply_total = 0
    buy_total = 0

    # Read and aggregate data
    with open(data_file_name, "r", encoding="utf-8") as src:
        for raw_line in src:
            line = raw_line.strip()
            if not line:
                # Skip empty lines
                continue

            # Expect exactly two fields separated by the first comma
            try:
                operation, amount_str = line.split(",", 1)
            except ValueError:
                # Skip malformed lines
                continue

            operation = operation.strip()
            amount_str = amount_str.strip()

            # Convert amount to integer, skip if invalid
            try:
                amount = int(amount_str)
            except ValueError:
                continue

            if operation == "supply":
                supply_total += amount
            elif operation == "buy":
                buy_total += amount
            else:
                # Ignore other operation types if present
                continue

    result = supply_total - buy_total

    # Prepare report content with a trailing newline at the end of file
    report_content = (
        f"supply,{supply_total}\n"
        f"buy,{buy_total}\n"
        f"result,{result}\n"
    )

    # Write the report
    with open(report_file_name, "w", encoding="utf-8") as dst:
        dst.write(report_content)
