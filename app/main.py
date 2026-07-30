def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name) as data_file:
        for line in data_file.readlines():
            separated_line = line.split(",")
            if separated_line[0] == "supply":
                supply += int(separated_line[1])
            elif separated_line[0] == "buy":
                buy += int(separated_line[1])

    result = supply - buy

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
