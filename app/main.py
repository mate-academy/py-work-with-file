def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name)
    dict_data = {"supply": 0, "buy": 0, "result": 0}
    for line in data_file:
        list_of_line = line.split(",")
        dict_data[list_of_line[0]] += int(list_of_line[1])
    dict_data["result"] = dict_data["supply"] - dict_data["buy"]
    report_file = open(report_file_name, "w")
    data = str(dict_data)
    data = data.replace("{", "")
    data = data.replace("}", "")
    data = data.replace("'", "")
    data = data.replace(",", "\n")
    data = data.replace(": ", ",")
    data = data.replace(" ", "")
    data += "\n"

    report_file.write(data)
