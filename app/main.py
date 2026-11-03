def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    # Read input file line by line using a context manager (memory efficient)
    with open(data_file_name, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # Skip empty lines

            if "," in line:
                parts = line.split(",", 1)
                operation = parts[0].strip().lower()
                try:
                    amount = int(parts[1].strip())
                except ValueError:
                    continue  # Skip lines with invalid numeric amounts

                if operation == "supply":
                    total_supply += amount
                elif operation == "buy":
                    total_buy += amount

    result = total_supply - total_buy

    # Write the report file with exact comma separation (no spaces)
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{result}\n")
