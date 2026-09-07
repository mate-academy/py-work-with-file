def create_report(data_file_name: str, report_file_name: str) -> None:
    total_buy = 0
    total_supply = 0
    with open(data_file_name, "r") as f:
        for line in f:
            line = line.rstrip()
            if not line:
                continue
            operation_type, amount = line.split(",")
            amount = int(amount)
            if operation_type == "buy":
                total_buy += amount
            elif operation_type == "supply":
                total_supply += amount
        result = total_supply - total_buy
    with open(report_file_name, "w") as f:
        f.write(f"supply,{total_supply}\n")
        f.write(f"buy,{total_buy}\n")
        f.write(f"result,{result}\n")
