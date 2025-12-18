def create_report(data_file_name: str, report_file_name: str) -> None:
    total_sell = 0
    total_supply = 0
    with open(data_file_name, "r") as file:
        for line in file:
            line = line.strip()

            operation, amount = line.split(",")
            if operation == "buy":
                total_sell += int(amount)
            elif operation == "supply":
                total_supply += int(amount)

    result = total_supply - total_sell
    with open(report_file_name, "w") as report:
        report.write(f"supply,{total_supply}\n")
        report.write(f"buy,{total_sell}\n")
        report.write(f"result,{result}\n")
