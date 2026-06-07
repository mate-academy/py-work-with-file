def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0
    with open(data_file_name, "r") as read_file:
        for line in read_file:
            line = line.strip()
            if line == "":
                continue
            line = line.split(",")
            operation = line[0]
            amount = line[1]
            amount = int(amount)
            if operation == "supply":
                total_supply += amount
            elif operation == "buy":
                total_buy += amount
    result = total_supply - total_buy
    with open(report_file_name, "w") as write_file:
        write_file.write(f"supply,{total_supply}\n"
                         f"buy,{total_buy}\n"
                         f"result,{result}\n")
