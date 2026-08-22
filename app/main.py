def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as data_file:
        supply = 0
        buy = 0

        for line in data_file.readlines():
            line_split = line.split(",")

            if line_split[0] == "supply":
                supply += int(line_split[1])
            if line_split[0] == "buy":
                buy += int(line_split[1])

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
