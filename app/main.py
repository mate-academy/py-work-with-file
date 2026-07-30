def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    # Read data from csv file
    with open(data_file_name, "r") as infile:
        for line in infile:
            line = line.strip()
            if not line:  # skip empty lines
                continue
            operation, amount_str = line.split(",")
            amount = int(amount_str)

            if operation == "supply":
                supply_total += amount
            elif operation == "buy":
                buy_total += amount

    result = supply_total - buy_total

    # Write report to output file
    with open(report_file_name, "w") as outfile:
        outfile.write(f"supply,{supply_total}\n")
        outfile.write(f"buy,{buy_total}\n")
        outfile.write(f"result,{result}\n")
