def create_report(data_file_name: str, report_file_name: str) -> None:
    file = open(data_file_name)
    lines = file.readlines()
    total_buy, total_supply = 0, 0
    for line in lines:
        line.strip()
        if line:
            operation, amount = line.split(",")
            amount = int(amount)
            if operation == "buy":
                total_buy += amount
            elif operation == "supply":
                total_supply += amount
    file.close()
    result = total_supply - total_buy
    file = open(report_file_name, "w")
    file.write(f"supply,{total_supply}\n")
    file.write(f"buy,{total_buy}\n")
    file.write(f"result,{result}\n")
