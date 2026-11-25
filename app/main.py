def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    # 1. Read the input CSV file line by line
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            # Strip whitespace/newlines and skip empty lines
            clean_line = line.strip()
            if not clean_line:
                continue

            # Split on the comma, convert amount to int, and add to totals
            operation, amount = clean_line.split(",")
            if operation == "supply":
                supply_total += int(amount)
            else:
                buy_total += int(amount)

    # 2. Calculate the final result
    result = supply_total - buy_total

    # 3. Write the formatted summary to the report file
    with open(report_file_name, "w") as report_file:
        # Write supply, buy, and result lines (ending with a newline)
        report_file.write(
            f"supply,{supply_total}\n"
            f"buy,{buy_total}\n"
            f"result,{result}\n"
        )
