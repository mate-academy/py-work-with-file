def create_report(
        data_file_name: str,
        report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    buy_value = 0
    supply_value = 0
    for line in data_file:
        split_line = line.split(",")
        if split_line[0] == "buy":
            buy_value += int(split_line[1])
        if split_line[0] == "supply":
            supply_value += int(split_line[1])
    data_file.close()
    result = supply_value - buy_value
    report = open(report_file_name, "w")
    report.write(f"supply,{supply_value}\n")
    report.write(f"buy,{buy_value}\n")
    report.write(f"result,{result}\n")
    report.close()
