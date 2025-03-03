def create_report(data_file_name: str, report_file_name: str) -> None:
    read = open(data_file_name, "r")
    dict_with_values = {}
    for char in read:
        list_ = char.replace("\n", "").split(",")
        if list_[0] in dict_with_values:
            dict_with_values[list_[0]] += int(list_[1])
        else:
            dict_with_values[list_[0]] = int(list_[1])
    read.close()
    result = dict_with_values["supply"] - dict_with_values["buy"]
    dict_with_values["result"] = result
    sorted(dict_with_values.items())
    writ = open(report_file_name, "w")
    writ.write(f"supply,{dict_with_values["supply"]}\n"
               f"buy,{dict_with_values["buy"]}\n"
               f"result,{dict_with_values["result"]}\n")
    writ.close()
