def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data,\
         open(report_file_name, "w") as report:
        dict_of_data = {}
        for i in data.read().split():
            if i.split(",")[0] not in dict_of_data:
                dict_of_data[i.split(",")[0]] = int(i.split(",")[1])
            else:
                dict_of_data[i.split(",")[0]] += int(i.split(",")[1])
        dict_of_data["result"] = dict_of_data["supply"] - dict_of_data["buy"]
        report.write(f"supply,{dict_of_data['supply']}\n"
                     f"buy,{dict_of_data['buy']}\n"
                     f"result,{dict_of_data['result']}\n")
