def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as input_file:
        for line in input_file:
            line = line.strip()
            if not line:
                continue

            operation, amount_str = line.split(",")
            amount_str = amount_str.strip()
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



