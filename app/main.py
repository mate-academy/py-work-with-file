def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    read_file = open(data_file_name)
    write_file = open(report_file_name, "w")
    supply = 0
    buy = 0
    for line in read_file.readlines():
        line = line.replace("\n", "").split(",")
        if "supply" in line:
            supply += int(line[1])
        else:
            buy += int(line[1])
    write_file.write("supply," + str(supply) + "\n")
    write_file.write("buy," + str(buy) + "\n")
    write_file.write("result," + str(supply - buy) + "\n")

    write_file.close()
    read_file.close()
