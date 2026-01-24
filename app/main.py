def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file1 = open(data_file_name)
    buy_sum = 0
    supply_sum = 0
    for line in data_file1:
        resline = line.strip().split(",")
        if resline[0] == "buy":
            buy_sum += int(resline[1])
        elif resline[0] == "supply":
            supply_sum += int(resline[1])
    data_file1.close()

    data_file2 = open(report_file_name, "w")

    data_file2.write(f"supply,{supply_sum}\n")

    data_file2.write(f"buy,{buy_sum}\n")

    data_file2.write(f"result,{supply_sum - buy_sum}\n")

    data_file2.close()
