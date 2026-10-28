def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    supply_sum:int = 0
    buy_sum:int = 0

    for line in data_file.readlines():
        split_line = line.strip().split(",")
        if "supply" in split_line:
            supply_sum += int(split_line[1])
        if "buy" in split_line:
            buy_sum += int(split_line[1])

    data_file.close()

    result_sum: int = supply_sum - buy_sum

    report_file = open(report_file_name, "w")
    report = f"supply,{supply_sum}\nbuy,{buy_sum}\nresult,{result_sum}\n"
    report_file.write(report)
    report_file.close()
