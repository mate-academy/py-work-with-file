def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    # Read the input CSV file
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.strip()
            if not line:  # Skip empty lines
                continue
            operation, amount = line.split(",")
            amount = int(amount)
            if operation == "supply":
                supply_total += amount
            elif operation == "buy":
                buy_total += amount

    # Calculate the result
    result = supply_total - buy_total

    # Write the report to the output CSV file
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buy_total}\n")
        report_file.write(f"result,{result}\n")
