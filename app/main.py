def create_report(data_file_name: str, report_file_name: str) -> None:
    file_r = open("C:\\Mate-Phyton-Projects\\py-work-with-file\\"
                  + data_file_name)

    supply_count = 0
    buy_count = 0

    for line in file_r:
        line_list = line.split(",")

        if line_list[0] == "supply":
            supply_count += int(line_list[1])

        if line_list[0] == "buy":
            buy_count += int(line_list[1])

    result = supply_count - buy_count
    print(result)

    file_w = open(report_file_name, "w")

    file_w.write("supply," + str(supply_count) + "\n")
    file_w.write("buy," + str(buy_count) + "\n")
    file_w.write("result," + str(result) + "\n")
