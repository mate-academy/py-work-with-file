def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0
    with open(data_file_name, mode="r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            operation_type, amount = line.split(",")
            amount = int(amount)
            if operation_type == "supply":
                total_supply += amount
            elif operation_type == "buy":
                total_buy += amount
    result = total_supply - total_buy
    with open(report_file_name, mode="w") as file:
        file.write(f"supply,{total_supply}\n")
        file.write(f"buy,{total_buy}\n")
        file.write(f"result,{result}\n")
