def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    file_open = open(data_file_name, "r")
    for line in file_open.readlines():
        line = line.split(",")
        if line[0] == "supply":
            supply += int(line[1])
        else:
            buy += int(line[1])
    file_open.close()
    file_write = open(report_file_name, "w")
    file_write.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
    file_write.close()
