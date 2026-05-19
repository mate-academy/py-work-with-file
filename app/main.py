def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    supply = 0
    buy = 0

    data_file = open(str(data_file_name), "r")
    for line in data_file:
        parts = line.split(",")
        if parts[0] == "supply":
            supply += int(parts[1])
        if parts[0] == "buy":
            buy += int(parts[1])
    data_file.close()

    result = supply - buy

    report_file = open(str(report_file_name), "w")
    report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
    report_file.close()
