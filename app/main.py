def create_report(data_file_name: str, report_file_name: str) -> None:
    file_data = open(data_file_name, "r")
    read_file = file_data.read()
    if read_file[-1] == "\n":
        read_file = read_file[:len(read_file) - 1]
    file_data.close()
    data = read_file.split("\n")
    data = [item.split(",") for item in data]
    dict_data = {}
    for item in data:
        if item[0] in dict_data:
            dict_data[item[0]] += int(item[1])
        else:
            dict_data[item[0]] = int(item[1])
    res = "supply" + "," + str(dict_data["supply"]) + "\n"
    res = res + "buy" + "," + str(dict_data["buy"]) + "\n"
    res = res + "result," + str(dict_data["supply"] - dict_data["buy"]) + "\n"
    file_report = open(report_file_name, "w")
    file_report.write(res)
    file_report.close()
