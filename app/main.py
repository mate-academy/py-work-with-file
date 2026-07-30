def create_report(data_file_name: str, report_file_name: str) -> None:
    file_date = open(data_file_name)
    file_report = open(report_file_name,"a")
    supply = 0
    buy = 0
    for line in file_date.readlines():
        line = line.strip()
        if not line:
            continue
        split_line = line.split(",")
        if split_line[0] == "supply":
            supply += int(split_line[1])
        if split_line[0] == "buy":
            buy += int(split_line[1])

    file_report.write(f"supply,{supply}\n")
    file_report.write(f"buy,{buy}\n")
    file_report.write(f"result,{supply - buy}\n")

    file_date.close()
    file_report.close()
