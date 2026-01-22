def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0
    with open(data_file_name, "r") as file:
        for line in file:
            if line.strip():
                operation, amount = line.strip().split(",")
                if operation == "supply":
                    total_supply += int(amount)
                elif operation == "buy":
                    total_buy += int(amount)

    with open(report_file_name, "w") as report:
        report.write(f"supply,{total_supply}\n")
        report.write(f"buy,{total_buy}\n")
        report.write(f"result,{total_supply - total_buy}\n")
