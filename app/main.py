def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as f:
        lines = f.readlines()
        for line in lines:
            operation, amount = line.split(",")
            amount = int(amount)
            if operation == "supply":
                total_supply += amount
            elif operation == "buy":
                total_buy += amount
    result = total_supply - total_buy

    with open(report_file_name, "w") as rf:
        rf.write(f"supply,{total_supply}\n")
        rf.write(f"buy,{total_buy}\n")
        rf.write(f"result,{result}\n")
