def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    data_file = open(data_file_name)
    for line in data_file:
        if line.strip().split(",")[0] == "supply":
            supply += int(line.strip().split(",")[1])
        if line.strip().split(",")[0] == "buy":
            buy += int(line.strip().split(",")[1])

    result = supply - buy
    data_file.close()
    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
    report_file.close()
