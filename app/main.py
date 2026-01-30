def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as read_file:
        for line in read_file:
            line_data = line.split(",")
            if line_data[0] == "buy":
                buy += int(line_data[1])
            else:
                supply += int(line_data[1])

    with open(report_file_name, "x") as write_file:
        write_file.write("supply," + str(supply) + "\n")
        write_file.write("buy," + str(buy) + "\n")
        write_file.write("result," + str(supply - buy) + "\n")
