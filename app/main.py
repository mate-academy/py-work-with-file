def create_report(data_file_name: str, report_file_name: str) -> None:
    file_to_read = open(data_file_name, "r")
    supply = 0
    buy = 0
    for line in file_to_read.readlines():
        line_list = line.split(",")
        if line_list[0] == "buy":
            buy += int(line_list[1])
        if line_list[0] == "supply":
            supply += int(line_list[1])
    result = supply - buy
    file_to_read.close()

    file_to_write = open(report_file_name, "w")
    file_to_write.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
    file_to_write.close()
