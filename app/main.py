def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0
    with open(data_file_name, "r") as data_file:
        for lines in data_file:
            split_line = lines.strip().split(",")
            if "supply" in split_line:
                total_supply += int(split_line[1])
            elif "buy" in split_line:
                total_buy += int(split_line[1])
            else:
                continue
    result = total_supply - total_buy

    with open(report_file_name, "a") as report_file:
        report_file.write("supply," + str(total_supply) + "\n")
        report_file.write("buy," + str(total_buy) + "\n")
        report_file.write("result," + str(result) + "\n")
