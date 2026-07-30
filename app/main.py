def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(f"{data_file_name}")
    supply = 0
    buy = 0

    for line in data_file:
        if line.split(",")[0] == "supply":
            supply += int(line.split(",")[-1])
        else:
            buy += int(line.split(",")[-1])

    data_file.close()
    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
    report_file.close()
