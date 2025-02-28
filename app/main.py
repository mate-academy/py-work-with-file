def create_report(
    data_file_name: str,
    report_file_name: str
) -> None:
    data_file = open(data_file_name, "r")
    report_file = open(report_file_name, "a")
    supply = 0
    buy = 0

    for line in data_file.readlines():
        splited_line = line.split(",")

        if splited_line[0] == "supply":
            supply += int(splited_line[1])

        if splited_line[0] == "buy":
            buy += int(splited_line[1])

    report_file.write(f"supply,{supply}\n")
    report_file.write(f"buy,{buy}\n")
    report_file.write(f"result,{supply - buy}\n")
    data_file.close()
    report_file.close()
