def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    data_file = open(data_file_name)
    for line in data_file.readlines():
        split_line = line.split(",")
        if "supply" in split_line:
            supply += int(split_line[1])
        if "buy" in split_line:
            buy += int(split_line[1])
    data_file.close()
    result = supply - buy
    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
    report_file.close()
