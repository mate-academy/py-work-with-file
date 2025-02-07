def create_report(data_file_name: str, report_file_name: str) -> None:
    datafile = open(data_file_name)
    datas = datafile.read().split("\n")
    result_dict = {"supply": 0, "buy": 0}
    for data in datas:
        splited_data = data.split(",")
        if splited_data[0] == "":
            continue
        result_dict[splited_data[0]] += int(splited_data[-1])
    datafile.close()

    reportfile = open(report_file_name, "w")
    supply = result_dict["supply"]
    buy = result_dict["buy"]
    reportfile.write(f"supply,{supply}\n")
    reportfile.write(f"buy,{buy}\n")
    reportfile.write(f"result,{supply - buy}\n")
    reportfile.close()
