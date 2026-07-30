def create_report(data_file_name: str, report_file_name: str) -> None:
    buy = 0
    supply = 0
    file_read = open(f"{data_file_name}")
    for line in file_read:
        read_line = line.split(",")
        if read_line[0] == "buy":
            buy += int(read_line[1])
        elif read_line[0] == "supply":
            supply += int(read_line[1])
    file_read.close()
    file_write = open(f"{report_file_name}", "w")
    file_write.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
    file_write.close()
