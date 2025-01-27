def create_report(data_file_name: str, report_file_name: str) -> None:
    # Read and process the data
    with open(data_file_name, "r") as data_file:
        total_supply = 0
        total_buy = 0

        for line in data_file:
            operation, amount = line.strip().split(",")
            if operation == "supply":
                total_supply += int(amount)
            elif operation == "buy":
                total_buy += int(amount)

    # Calculate result
    result = total_supply - total_buy

    # Write the report
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{result}\n")
