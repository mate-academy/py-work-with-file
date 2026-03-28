def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name) as f:
        for line in f.readlines():
            separated_line = line.split(",")
            if separated_line[0] == "supply":
                supply += int(separated_line[1])
            else:
                buy += int(separated_line[1])

    result = supply - buy
    report = open(report_file_name, "w")
    report.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
    report.close()
