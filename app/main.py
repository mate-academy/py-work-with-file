def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name)
    supply_sum = 0
    buy_sum = 0
    result = 0
    for line in data_file.readlines():
        garbage_list = line.split(",")
        if garbage_list[0] == "supply":
            supply_sum += int(garbage_list[1])
        else:
            buy_sum += int(garbage_list[1])

    result = supply_sum - buy_sum

    report_file = open(report_file_name, "w")

    report_file.write(f"supply,{supply_sum}\nbuy,{buy_sum}\nresult,{result}\n")

    data_file.close()
    report_file.close()
