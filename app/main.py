def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        lines = data_file.readlines()
    supply_count = 0
    buy_count = 0
    for line in lines:
        variables = line.split(",")
        if variables[0] == "supply":
            supply_count += int(variables[1])
        elif variables[0] == "buy":
            buy_count += int(variables[1])
    report_lines = [
        f"supply,{supply_count}\n",
        f"buy,{buy_count}\n",
        f"result,{supply_count - buy_count}\n"
    ]
    with open(report_file_name, "w") as report_file:
        report_file.writelines(report_lines)
