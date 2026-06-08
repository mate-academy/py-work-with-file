def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name) as data_file:
        for line in data_file:
            line = line.strip().split(",")
            if line[0] == "supply":
                supply += int(line[1])
            if line[0] == "buy":
                buy += int(line[1])

    result = supply - buy

    with open(report_file_name, "w") as report_file:
        report_file.write("supply," + str(supply) + "\n")
        report_file.write("buy," + str(buy) + "\n")
        report_file.write("result," + str(result) + "\n")
