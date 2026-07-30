def create_report(data_file_name: str, report_file_name: str) -> None:
    total_buy = 0
    total_supply = 0

    with open(data_file_name, "r") as input_file:
        for line in input_file:
            clean_line = line.strip()
            if not clean_line:
                continue
            operation, amount_str = clean_line.split(",")
            amount = int(amount_str)

            if operation == "supply":
                total_supply += amount
            elif operation == "buy":
                total_buy += amount
    result = total_supply - total_buy

    with open(report_file_name, "w") as output_file:
        output_file.write(f"supply,{total_supply}\n")
        output_file.write(f"buy,{total_buy}\n")
        output_file.write(f"result,{result}\n")
