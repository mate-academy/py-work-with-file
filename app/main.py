def create_report(data_file_name: str, report_file_name: str) -> None:

    data_file = open(data_file_name)
    supply = 0
    buy = 0

    for line in data_file:
        part = line.strip().split(",")
        if part[0] == "supply":
            supply += int(part[1])
        elif part[0] == "buy":
            buy += int(part[1])

    data_file.close()

    result = f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n"

    file_report = open(report_file_name, "w")
    file_report.write(result)
    file_report.close()
