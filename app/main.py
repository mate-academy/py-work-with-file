def create_report(data_file_name: str, report_file_name: str) -> None:
    t_supply = 0
    t_buy = 0
    with open(data_file_name, "r") as data_file:
        for lines in data_file:
            split_line = lines.strip().split(",")
            if "supply" in split_line:
                t_supply += int(split_line[1])
            elif "buy" in split_line:
                t_buy += int(split_line[1])
            else:
                continue
        result = t_supply - t_buy

        with open(report_file_name, "w") as report_file:
            report_file.write("supply," + str(t_supply) + "\n")
            report_file.write("buy," + str(t_buy) + "\n")
            report_file.write("result," + str(result) + "\n")
