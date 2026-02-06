def create_report(data_file_name: str, report_file_name: str) -> None:
    dict_result = {"supply": 0, "buy": 0, "result": 0}
    file_data = open(data_file_name)
    for line in file_data.readlines():
        dict_result[line.split(",")[0]] += int(line.split(",")[1])
    dict_result["result"] = dict_result["supply"] - dict_result["buy"]
    file_data.close()
    file_report = open(report_file_name, "w")
    for key, value in dict_result.items():
        file_report.write(f"{key},{value}\n")
    file_report.close()
