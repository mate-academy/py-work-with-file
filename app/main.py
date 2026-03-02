def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = buy = 0
    with open(data_file_name) as r_file:
        data_list = r_file.readlines()

    for data_line in data_list:
        data_line = data_line[:-1]
        item = data_line.split(",")

        if item[0] == "supply":
            supply += int(item[1])
        else:
            buy += int(item[1])

    report_data = ("supply" + ","
                   + f"{supply}\nbuy" + ","
                   + f"{buy}\nresult" + ","
                   + f"{supply - buy}\n")

    with open(report_file_name, "w") as w_file:
        w_file.write(report_data)
