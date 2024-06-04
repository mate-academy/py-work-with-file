def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as file:
        for line in file:
            line_split = line.split(",")
            operation, value = line_split[0], int(line_split[1])
            if operation == "supply":
                total_supply += value
            else:
                total_buy += value
    result = total_supply - total_buy

    with open(report_file_name, "w") as report:
        report.write(f"supply,{total_supply}\n")
        report.write(f"buy,{total_buy}\n")
        report.write(f"result,{result}\n")