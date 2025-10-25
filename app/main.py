def create_report(data_file_name: str, report_file: str) -> None:
    data_dict = {"supply": 0, "buy": 0, }
    data = open(data_file_name, "r")
    for line in data :
        data_dict[line.split(",")[0]] += int(line.split(",")[1])
    data.close()
    data_dict["result"] = data_dict["supply"] - data_dict["buy"]
    report = open(report_file, "w")
    for key, value in data_dict.items() :
        report.write(key + "," + str(value) + "\n")
    report.close()
