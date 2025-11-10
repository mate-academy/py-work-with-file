def create_report(data_file_name: str, report_file_name: str) -> None:
    data = open(data_file_name, "r")
    supply = 0
    buy = 0

    for line in data:
        if line.split(",")[0] == "supply":
            supply += int(line.split(",")[1])
        elif line.split(",")[0] == "buy":
            buy += int(line.split(",")[1])

    data.close()
    report = open(report_file_name, "a")
    report.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
