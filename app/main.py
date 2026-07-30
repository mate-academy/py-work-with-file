def create_report(data_file_name: str, report_file_name: str) -> None:
    info_file = open(data_file_name)
    report_file = open(report_file_name, "w")
    supply, buy, result = 0, 0, 0
    for line in info_file:
        name, value = line.strip().split(",")
        if name == "supply":
            supply += int(value)
        elif name == "buy":
            buy += int(value)
    result = supply - buy
    report_file.write(f"supply,{supply}\n")
    report_file.write(f"buy,{buy}\n")
    report_file.write(f"result,{result}\n")
    info_file.close()
    report_file.close()
