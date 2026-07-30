def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    data_file = open(data_file_name, "r")
    for line in data_file.readlines():
        splitted_line = line.split(",")
        if "supply" == splitted_line[0]:
            supply += int(splitted_line[1])
        elif "buy" == splitted_line[0]:
            buy += int(splitted_line[1])
    data_file.close()
    report_file = open(report_file_name, "w")
    report_file.write("supply," + str(supply) + "\n")
    report_file.write("buy," + str(buy) + "\n")
    report_file.write("result," + str(supply - buy) + "\n")
    report_file.close()
