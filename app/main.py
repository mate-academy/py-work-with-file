def create_report(data_file_name: str, report_file_name: str) -> None:
    input_file = open(data_file_name, "r")
    supply = 0
    buy = 0
    for line in input_file.readlines():
        if line == "":
            break
        splitted_line = line.split(",")
        if splitted_line[0] == "supply":
            supply += int(splitted_line[1])
        elif splitted_line[0] == "buy":
            buy += int(splitted_line[1])
    result = supply - buy
    input_file.close()
    report_file = open(report_file_name, mode="w")
    report_file.write(f"supply,{supply}\n")
    report_file.write(f"buy,{buy}\n")
    report_file.write(f"result,{result}\n")
    report_file.close()
