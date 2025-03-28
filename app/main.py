def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    all_lines = []
    for line in data_file.readlines():
        all_lines.append(line)
    data_file.close()

    factors_dict = {"supply": [], "buy": []}
    for line in all_lines:
        columns = line.split(",")
        factors_dict[columns[0]].append(int(columns[1]))

    supply_sum = sum(factors_dict["supply"])
    buy_sum = sum(factors_dict["buy"])

    supply_line = f"supply,{sum(factors_dict['supply'])}"
    buy_line = f"buy,{sum(factors_dict['buy'])}"
    result_line = f"result,{supply_sum - buy_sum}"
    line_to_write = "\n".join([supply_line, buy_line, result_line, ""])

    report_file = open(report_file_name, "w")
    report_file.writelines(line_to_write)
    report_file.close()
