def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0
    with open(data_file_name, "r") as file:
        for line in file:
            if not line.strip():
                continue
            operation, amount = line.strip().split(",")
            amount = int(amount)
            if operation == "buy":
                total_buy += amount
            if operation == "supply":
                total_supply += amount
        result = total_supply - total_buy
        file.close()

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{result}\n")
