def create_report(data_file_name: str, report_file_name: str) -> None:
    f = open(data_file_name)
    datas = f.read().split("\n")
    result_dict = {}
    for data in datas:
        splited_data = data.split(",")
        if splited_data[0] in result_dict:
            if splited_data[0] == "":
                continue
            result_dict[splited_data[0]] += int(splited_data[-1])
        else:
            if splited_data[0] == "":
                continue
            result_dict[splited_data[0]] = int(splited_data[-1])
    f.close()

    f = open(report_file_name, "w")
    f.write(f"supply,{result_dict["supply"]}\n")
    f.write(f"buy,{result_dict["buy"]}\n")
    f.write(f"result,{result_dict["supply"] - result_dict["buy"]}\n")
    f.close()
