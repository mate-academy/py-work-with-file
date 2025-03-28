def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    data_storage = data_file.readlines()
    data_file.close()
    supply = 0
    buy = 0
    for one_line in data_storage:
        one_line_list = one_line.split(",")
        if one_line_list[0] == "supply":
            supply += int(one_line_list[1][: - 1])
        elif one_line_list[0] == "buy":
            buy += int(one_line_list[1][: - 1])
    data_file.close()
    report_file = open(report_file_name, "w")
    prefix = "supply,"
    report_file.write(f"{prefix}{supply}\n")
    prefix = "buy,"
    report_file.write(f"{prefix}{buy}\n")
    prefix = "result,"
    report_file.write(f"{prefix}{supply - buy}\n")
    report_file.close()
