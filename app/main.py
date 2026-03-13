def create_report(data_file_name: str, report_file_name: str) -> None:
    one_file = open(data_file_name, "r")
    supply = 0
    buy = 0
    for line in one_file.readlines():
        list_str = line.split(",")
        if list_str[0] == "supply":
            supply += int(list_str[1])
        if list_str[0] == "buy":
            buy += int(list_str[1])
    one_file.close()
    result = supply - buy
    report = open(report_file_name, "w")
    report.write(f"supply,{supply}\n")
    report.write(f"buy,{buy}\n")
    report.write(f"result,{result}\n")
    report.close()
