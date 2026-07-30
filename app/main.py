def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name) as data_file:
        for line in data_file:
            line_data = line.split(",")
            if line_data[0] == "supply":
                supply += int(line_data[1])
            elif line_data[0] == "buy":
                buy += int(line_data[1])

    with open(report_file_name, "w") as report_file:
        report_file.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{supply - buy}\n"
        )
