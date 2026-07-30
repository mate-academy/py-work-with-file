def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    data_file = open(data_file_name, "r")
    for line in data_file:
        line = line.strip()
        if not line:
            continue

        operation, amount = line.split(",")
        amount = int(amount)

        if operation == "supply":
            total_supply += amount
        elif operation == "buy":
            total_buy += amount

    data_file.close()

    result = total_supply - total_buy

    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{total_supply}\n")
    report_file.write(f"buy,{total_buy}\n")
    report_file.write(f"result,{result}\n")
    report_file.close()
