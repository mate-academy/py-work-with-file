def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    data_file = open(data_file_name, "r")
    for line in data_file:
        line_variable = line.strip()
        line_variable_list = line_variable.split(",")
        if line_variable_list[0] == "supply":
            supply += int(line_variable_list[1])
        elif line_variable_list[0] == "buy":
            buy += int(line_variable_list[1])
    result = supply - buy

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{result}\n")

    data_file.close()
    report_file.close()
