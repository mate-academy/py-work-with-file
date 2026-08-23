def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    supply = 0
    buy = 0
    for line in data_file.readlines():
        line = line.split(",")
        if line[0] == "supply":
            supply += int(line[1])
        if line[0] == "buy":
            buy += int(line[1])
    result = supply - buy
    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
