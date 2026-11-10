def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    supply = 0
    buy = 0

    for line in data_file.readlines():
        line_list = line.split(",")
        if line_list[0] == "supply":
            supply += int(line_list[1])
        elif line_list[0] == "buy":
            buy += int(line_list[1])
    data_file.close()
    result = supply - buy

    report = open(report_file_name, "w")
    report.write(f"supply,{supply}\n")
    report.write(f"buy,{buy}\n")
    report.write(f"result,{result}\n")
    report.close()
