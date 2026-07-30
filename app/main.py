def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as data:
        for line in data:
            if line.strip() == "":
                continue
            operation, amount = line.split(",")
            if operation == "supply":
                total_supply += int(amount)
            elif operation == "buy":
                total_buy += int(amount)

    with open(report_file_name, "w") as report:
        result = total_supply - total_buy
        report.write(f"supply,{total_supply}\n")
        report.write(f"buy,{total_buy}\n")
        report.write(f"result,{result}\n")
