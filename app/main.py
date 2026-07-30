def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file_info = open(data_file_name)
    supply = 0
    buy = 0
    for line in data_file_info:
        supply_list = line.split(",")
        number = supply_list[-1].strip()
        if "supply" in line:
            supply += int(number)
        elif "buy" in line:
            buy += int(number)

    result = supply - buy
    report_file_info = open(report_file_name, mode="w")
    report_file_info.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
