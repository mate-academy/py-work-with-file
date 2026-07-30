def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    data_file = open(data_file_name, "r")
    for line in data_file:
        line_data = line.split(",")
        if line_data[0] == "supply":
            supply += int(line_data[1].strip("\n"))
        if line_data[0] == "buy":
            buy += int(line_data[1].strip("\n"))
    data_file.close()
    result_file = open(report_file_name, "w")
    result_file.write(f"supply,{supply}\n")
    result_file.write(f"buy,{buy}\n")
    result = supply - buy
    result_file.write(f"result,{result}\n")
    result_file.close()
