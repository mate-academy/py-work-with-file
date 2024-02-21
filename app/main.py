def create_report(data_file_name: str, report_file_name: str) -> any:
    with open(data_file_name, "r") as data,\
            open(report_file_name, "a") as report:
        buy = 0
        supply = 0

        for line in data.readlines():
            if "buy" in line:
                buy += int(line.split(",")[1][0:-1])
            if "supply" in line:
                supply += int(line.split(",")[1][0:-1])

        result = supply - buy

        report.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
