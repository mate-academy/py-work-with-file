def create_report(data_file_name: str,
                  report_file_name: str):
    with open(data_file_name, "r") as data, \
            open(report_file_name, "w") as report:
        supply, buy = 0, 0
        for line in data:
            line = line.split(",")
            if line[0] == "supply":
                supply += int(line[1])
            elif line[0] == "buy":
                buy += int(line[1])

        result = supply - buy
        report.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
