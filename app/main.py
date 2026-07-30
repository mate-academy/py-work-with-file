def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0
    with open(data_file_name) as data_file:
        for line in data_file:
            line_list = line.strip().split(",")
            if line_list[0] == "supply":
                total_supply += int(line_list[1])
            elif line_list[0] == "buy":
                total_buy += int(line_list[1])
    result = total_supply - total_buy
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{result}\n")
