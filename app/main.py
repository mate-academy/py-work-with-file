def create_report(data_file_name: str, report_file_name: str) -> None:
    file_input = open(data_file_name, "tr")
    supply = 0
    buy = 0
    for line in file_input.readlines():
        line_list = line.split(",")
        if line_list[0] == "supply":
            supply += int(line_list[1])
        if line_list[0] == "buy":
            buy += int(line_list[1])
    file_input.close()

    file_output = open(report_file_name, "tw")
    report_output = ("supply,"
                     + f"{supply}\nbuy,"
                     + f"{buy}\nresult,"
                     + f"{supply - buy}\n"
                     )
    file_output.write(report_output)
    file_output.close()
