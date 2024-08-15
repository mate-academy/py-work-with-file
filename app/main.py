def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    data_file = open(data_file_name, "r")
    for line in data_file:
        operation, amount = line.split(",")
        amount = int(amount)

        if operation == "supply":
            total_supply += amount
        elif operation == "buy":
            total_buy += amount

    result = total_supply - total_buy

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{result}\n")
