def create_report(data_file_name: str, report_file_name: str) -> None:
    data_dict = {}
    with open(data_file_name, "r") as data, open(report_file_name, "w") as rep:
        for line in data:
            if line.split(",")[0] in data_dict.keys():
                data_dict[line.split(",")[0]] += int(line.split(",")[1])
            else:
                data_dict[line.split(",")[0]] = int(line.split(",")[1])
        data_dict["result"] = data_dict["supply"] - data_dict["buy"]
        rep.write(
            f"supply,{data_dict['supply']}\n"
            f"buy,{data_dict['buy']}\n"
            f"result,{data_dict['result']}\n"
        )
