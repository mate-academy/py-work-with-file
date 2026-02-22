def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    input_file = open(data_file_name, "r")
    supply_sum = 0
    buy_sum = 0
    for line in input_file:
        spl_line = line.split(",")
        if spl_line[0] == "supply":
            supply_sum += int(spl_line[1])
        if spl_line[0] == "buy":
            buy_sum += int(spl_line[1])
    input_file.close()
    output_file = open(report_file_name, "w")
    output_file.write(f"supply,{supply_sum}\n")
    output_file.write(f"buy,{buy_sum}\n")
    output_file.write(f"result,{supply_sum - buy_sum}\n")
    output_file.close()
