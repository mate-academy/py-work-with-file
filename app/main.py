def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    # Open the input CSV file in read mode using a context manager
    with open(data_file_name, "r") as file:
        # Iterate through the file line by line (memory-efficient reading)
        for line in file:
            line = line.strip()
            if not line:
                continue  # Skip empty or trailing lines as required

            # Split by comma and strip whitespace around parts
            parts = line.split(",")
            if len(parts) == 2:
                operation = parts[0].strip()
                amount = int(parts[1].strip())

                if operation == "supply":
                    total_supply += amount
                elif operation == "buy":
                    total_buy += amount

    # Calculate the final result
    result = total_supply - total_buy

    # Write the report to the output file
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply , {total_supply}\n")
        report_file.write(f"buy , {total_buy}\n")
        report_file.write(f"result , {result}\n")
