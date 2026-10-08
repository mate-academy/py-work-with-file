def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    # Read data from the input file
    with open(data_file_name, "r") as file:
        for line in file:
            # Skip empty lines, especially at the end of the file
            line = line.strip()
            if not line:
                continue

            operation, amount_str = line.split(",")
            amount = int(amount_str)

            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount

    result = supply - buy

    # Write the calculated report to the output file
    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply}\n")
        file.write(f"buy,{buy}\n")
        file.write(f"result,{result}\n")
