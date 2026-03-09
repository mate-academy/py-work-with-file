def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total: int = 0
    buy_total: int = 0

    # 1. Read input file and accumulate totals
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            # Clean and skip empty lines
            line = line.strip()
            if not line:
                continue

            # Parse CSV format: operation,amount
            operation, amount = line.split(",")

            if operation == "supply":
                supply_total += int(amount)
            elif operation == "buy":
                buy_total += int(amount)

    # 2. Write the computed report to the output file
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buy_total}\n")
        report_file.write(f"result,{supply_total - buy_total}\n")
