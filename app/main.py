def create_report(data_file_name: str, report_file_name: str) -> None:
    data_dict = {"supply": 0, "buy": 0, "result": 0}
    data_file = open(data_file_name)

    for element in data_file:
        element_lst = element.split(",")
        data_dict[element_lst[0]] += int(element_lst[1])
    data_file.close()

    data_dict["result"] = data_dict["supply"] - data_dict["buy"]

    report_file = open(report_file_name, "w")
    for key, value in data_dict.items():
        report_file.write(f"{key},{str(value)}\n")
    report_file.close()
