def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name)
    supply = 0
    buy = 0

    for line in data_file.readlines():
        if "supply" in line:
            supply += int(line.split(",")[1])
        else:
            buy += int(line.split(",")[1])
    data_file.close()

    report = open(report_file_name, "w+")

    report.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
    report.close()
