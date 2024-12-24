def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_num = 0
    buy_num = 0
    with open(data_file_name, "r") as f:
        for line in f:
            line_list = line.strip().split(",")
            if line_list[0] == "supply":
                supply_num += int(line_list[1])
            elif line_list[0] == "buy":
                buy_num += int(line_list[1])
        result = supply_num - buy_num
    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply_num}\n")
        f.write(f"buy,{buy_num}\n")
        f.write(f"result,{result}\n")
