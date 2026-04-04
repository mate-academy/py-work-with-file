def create_report(data_file_name: str, report_file_name: str):
    result_dict = {"supply": 0,
                   "buy": 0}
    with open(data_file_name, "r") as f:
        for line in f:
            line_split = line.strip().split(",")
            result_dict[line_split[0]] += int(line_split[1])
    result_dict["result"] = f'{result_dict["supply"] - result_dict["buy"]}'
    result_record = ""
    for key, value in result_dict.items():
        result_record += str(key) + "," + str(value) + "\n"
    with open(report_file_name, "w") as rfn:
        rfn.write(result_record)
