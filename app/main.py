def create_report(data_file_name: str, report_file_name: str) -> None:
    buy = 0
    supply = 0
    data_file = open(data_file_name, "r")
    for line in data_file:
        if "buy" in line:
            buy += int(line.split(",")[1])
        if "supply" in line:
            supply += int(line.split(",")[1])
    data_file.close()
    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
