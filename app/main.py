def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as input_data:
        supply = 0
        buy = 0
        for line in input_data.readlines():
            line_split = line.split(",")
            if line_split[0] == "supply":
                supply += int(line_split[1])
            if line_split[0] == "buy":
                buy += int(line_split[1])
        result = supply - buy
    with open(report_file_name, "a") as report:
        report.write(f"supply,{supply}\n")
        report.write(f"buy,{buy}\n")
        report.write(f"result,{result}\n")
