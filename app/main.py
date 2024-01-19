def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        for line in file.readlines():
            line = line.split(",")
            if line[0] == "supply":
                supply += int(line[1])
            else:
                buy += int(line[1])

    result = supply - buy

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
