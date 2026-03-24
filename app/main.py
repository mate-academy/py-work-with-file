def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as input_file:
        for line in input_file:
            line = line.strip()
            if not line:
                continue
            parts = [p.strip() for p in line.split(",")]
            if len(parts) != 2:
                continue
            operation, amount_str = parts
            try:
                amount = int(amount_str)
            except ValueError:
                continue
            if operation == "supply":
                total_supply += amount
            elif operation == "buy":
                total_buy += amount

    result = total_supply - total_buy

    with open(report_file_name, "w") as output_file:
        output_file.write(f"supply,{total_supply}\n")
        output_file.write(f"buy,{total_buy}\n")
        output_file.write(f"result,{result}\n")
