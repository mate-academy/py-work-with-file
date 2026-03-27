def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    report_file = open(report_file_name, "a")
    supply, buy = 0, 0
    for line in data_file:
        line = line.split(",")
        if line[0] == "supply":
            supply += int(line[1])
        elif line[0] == "buy":
            buy += int(line[1])
    report_file.write(f"supply,{supply}\n")
    report_file.write(f"buy,{buy}\n")
    report_file.write(f"result,{supply - buy}\n")
    report_file.close()
    data_file.close()
