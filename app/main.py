def create_report(data_file_name: str, report_file_name: str) -> None:
    f = open(data_file_name)
    datas = f.read().split("\n")
    result_dict = {"supply": 0, "buy": 0}
    for data in datas:
        splited_data = data.split(",")
        if splited_data[0] == "":
            continue
        result_dict[splited_data[0]] += int(splited_data[-1])
    f.close()

    f = open(report_file_name, "w")
    f.write(f"supply,{result_dict["supply"]}\n")
    f.write(f"buy,{result_dict["buy"]}\n")
    f.write(f"result,{result_dict["supply"] - result_dict["buy"]}\n")
    f.close()
