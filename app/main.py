def create_report(data_file_name:str, report_file_name:str) -> None:
    data_file = open(data_file_name, "r")
    supply = 0
    buy = 0
    for line in data_file.readlines():
        line = line.strip()
        if not line:
            continue
        result = line.split(",")
        if result[0] == "supply":
            supply += int(result[1])
        elif result[0] == "buy":
            buy += int(result[1])
    report = open(report_file_name, "w")
    report.write("supply," + str(supply) + "\n")
    report.write("buy," + str(buy) + "\n")
    report.write("result," + str(supply - buy) + "\n")
    data_file.close()
    report.close()
