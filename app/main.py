def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with open(data_file_name, "r") as data:
        supply = 0
        buy = 0
        for line in data:
            line_info = line.split(",")
            if line_info[0] == "supply":
                supply += int(line_info[1])
            else:
                buy += int(line_info[1])

    with open(report_file_name, "a") as report:
        report.write(f"supply,{supply}\n")
        report.write(f"buy,{buy}\n")
        report.write(f"result,{supply - buy}\n")
