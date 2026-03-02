from typing import NoReturn


def create_report(data_file_name: str, report_file_name: str) -> NoReturn:
    supply_total: int = 0
    buy_total: int = 0

    # Step 1: Read the input CSV file
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.strip()
            if line:  # Skip empty lines
                operation, amount_str = line.split(",")
                amount = int(amount_str)

                # Step 2: Accumulate totals based on operation type
                if operation == "supply":
                    supply_total += amount
                elif operation == "buy":
                    buy_total += amount

    # Step 3: Calculate result
    result: int = supply_total - buy_total

    # Step 4: Write the report to the output file without spaces after commas
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buy_total}\n")
        report_file.write(f"result,{result}\n")
