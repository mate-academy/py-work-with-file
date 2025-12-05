def create_report(data_file_name: str, report_file_name: str) -> None:
    in_file = open(data_file_name, "r")
    buy_cnt = 0
    supply_cnt = 0
    for line in in_file.readlines():
        if line.split(",")[0] == "buy":
            buy_cnt += int(line.split(",")[1])
        if line.split(",")[0] == "supply":
            supply_cnt += int(line.split(",")[1])
    result = supply_cnt - buy_cnt

    out_file = open(report_file_name, "w")
    out_file.write(f"supply,{supply_cnt}\n")
    out_file.write(f"buy,{buy_cnt}\n")
    out_file.write(f"result,{result}\n")
    in_file.close()
    out_file.close()
