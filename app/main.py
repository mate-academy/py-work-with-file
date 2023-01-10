def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file, \
            open(report_file_name, "a") as report_file:
        supply, buy = 0, 0
        for line in data_file:
            if len(line) == 0:
                break
            report = line.split(",")
            if report[0] == "supply":
                supply += int(report[1])
            if report[0] == "buy":
                buy += int(report[1])

        result = supply - buy
        report_file.write("supply," + str(supply) + "\n")
        report_file.write("buy," + str(buy) + "\n")
        report_file.write("result," + str(result) + "\n")
