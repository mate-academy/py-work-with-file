def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    data_dict = {}
    for line in data_file.readlines():
        if line.split(",")[0] in data_dict:
            data_dict[line.split(",")[0]] += int(line.split(",")[1])
        else:
            data_dict[line.split(",")[0]] = int(line.split(",")[1])
    data_dict["result"] = data_dict["supply"] - data_dict["buy"]
    data_file.close()
    result_file = open(report_file_name, "a")
    result_file.write(f"supply,{data_dict['supply']}\n")
    result_file.write(f"buy,{data_dict['buy']}\n")
    result_file.write(f"result,{data_dict['result']}\n")
    result_file.close()
