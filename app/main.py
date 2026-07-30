def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        total_supply = 0
        total_buy = 0
        for line in file:
            parts = line.split(",")
            operation = parts[0]
            amount = int(parts[1])
            if operation == "supply":
                total_supply += amount
            elif operation == "buy":
                total_buy += amount
        result = total_supply - total_buy

    with open(report_file_name, "w") as f:
        f.write(f"supply,{total_supply}\n")
        f.write(f"buy,{total_buy}\n")
        f.write(f"result,{result}\n")
