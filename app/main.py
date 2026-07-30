def create_report(data_file_name: str, report_file_name: str) -> None:
    # data reading
    buy = 0
    supply = 0

    r_file = open(data_file_name, "r")
    for line in r_file.readlines():
        info = line.split(",")
        if info[0] == "buy":
            buy += int(info[1])
        elif info[0] == "supply":
            supply += int(info[1])

    result = supply - buy
    r_file.close()

    # report writing
    w_file = open(report_file_name, "w")
    w_file.write("supply," + str(supply) + "\n")
    w_file.write("buy," + str(buy) + "\n")
    w_file.write("result," + str(result) + "\n")
    w_file.close()
