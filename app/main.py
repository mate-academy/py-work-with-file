def create_report(data_file_name: str, report_file_name: str) -> int:
    total_supply = 0
    total_buy = 0
    with open(data_file_name, "r") as file_in:
        for line in file_in:
            parts = line.split(",")
            operation_type, amount = parts[0], int(parts[1])
            if operation_type == "supply":
                total_supply += amount
            elif operation_type == "buy":
                total_buy += amount

    result = total_supply - total_buy

    with open(report_file_name, "w") as file:
        file.write(f"supply,{total_supply}\n")
        file.write(f"buy,{total_buy}\n")
        file.write(f"result,{result}\n")
