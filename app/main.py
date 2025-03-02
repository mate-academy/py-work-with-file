def create_report(data_file_name: str, report_file_name: str) -> None:
    data = open(data_file_name, "tr")
    data_dict = {}
    for element in data:
        element_list = element.split(",")
        if element_list[0] in data_dict:
            data_dict[element_list[0]] += int(element_list[1])
        else:
            data_dict[element_list[0]] = int(element_list[1])
    data_dict["result"] = data_dict["supply"] - data_dict["buy"]
    data.close()
    report = open(report_file_name, "w")
    report.write(f"supply,{data_dict["supply"]}\n"  # noqa: E231
                 f"buy,{data_dict["buy"]}\n"  # noqa: E231
                 f"result,{data_dict["result"]}\n")  # noqa: E231
    report.close()
