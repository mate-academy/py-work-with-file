def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file_open = open(data_file_name)
    supply_sum = 0
    buy_sum = 0
    for line in data_file_open:
        line_split = line.split(",")
        if line_split[0] == "supply":
            supply_sum += int(line_split[1])
        if line_split[0] == "buy":
            buy_sum += int(line_split[1])
    data_file_open.close()
    report_file_open = open(report_file_name, "w")
    report_file_open.write(f"supply,{supply_sum}\n"
                           f"buy,{buy_sum}\n"
                           f"result,{supply_sum - buy_sum}\n")
    report_file_open.close()
