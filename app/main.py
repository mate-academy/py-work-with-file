def create_report(data_file_name: str, report_file_name: str) -> None:
    info = open(data_file_name,"r")
    need_add_result = open(report_file_name,"a")
    result = {
        "supply": 0,
        "buy": 0}
    for line in info.readlines():
        line_ = line.split(",")
        line_[1] = int(line_[1].replace("\n",""))
        result[line_[0]] += line_[1]
    first_line = f"supply,{result['supply']}\n"
    second_line = f"buy,{result['buy']}\n"
    third_line = f"result,{result['supply'] - result['buy']}\n"
    need_add_result.write(first_line)
    need_add_result.write(second_line)
    need_add_result.write(third_line)
    print(need_add_result)
