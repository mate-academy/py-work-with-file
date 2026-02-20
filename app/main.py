def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                operation, value = line.split(",")
                value = int(value)
                if operation == "supply":
                    total_supply += value
                elif operation == "buy":
                    total_buy += value

    with open(report_file_name, "w") as report:
        report.write(f"supply,{total_supply}\n")
        report.write(f"buy,{total_buy}\n")
        report.write(f"result,{total_supply - total_buy}\n")
