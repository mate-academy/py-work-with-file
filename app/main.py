def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as csv_file:
        for line in csv_file:
            if not line:
                pass
            line_list = line.split(",")
            if line_list[0] == "supply":
                supply += int(line_list[1])
            elif line_list[0] == "buy":
                buy += int(line_list[1])

    result = supply - buy

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\n"
                     f"buy,{buy}\n"
                     f"result,{result}\n")
