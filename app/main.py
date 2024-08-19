def create_report(data_file_name: str, report_file_name: str) -> None:
    working_file = open(data_file_name, "r")
    report = open(report_file_name, "+w")
    supply = 0
    buy = 0
    result = 0
    for line in working_file:
        line_list = line.split(",")
        if "supply" in line_list:
            supply += int(line_list[-1])
        if "buy" in line_list:
            buy += int(line_list[-1])
    result = supply - buy
    report.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
    working_file.close()
    report.close()


create_report("apples.csv", "apples_report.csv")
