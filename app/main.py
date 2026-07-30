def create_report(data_file_name: str, report_file_name: str) -> None:
    supply, buy = 0, 0
    with open(data_file_name, "r") as data_file:
        data = data_file.readlines()
    for line in data:
        line_data = line.split(",")
        if line_data[0] == "supply":
            supply += int(line_data[1])
        if line_data[0] == "buy":
            buy += int(line_data[1])
    result = supply - buy
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{result}\n")
