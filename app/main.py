def create_report(data_file_name: str, report_file_name: str) -> None:
    supply, buy, result = 0, 0, 0

    with open(data_file_name, "r") as data:
        for line in data:
            line = line.replace("\n", "").split(",")

            if line[0] == "supply":
                supply += int(line[1])
            elif line[0] == "buy":
                buy += int(line[1])
    result = supply - buy

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\n"
                     f"buy,{buy}\n"
                     f"result,{result}\n")
