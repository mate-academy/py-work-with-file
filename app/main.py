def create_report(data_file_name: str, report_file_name: str) -> None:
    data = open(data_file_name)

    data_dict = {}

    for string in data:
        if not string:
            break
        data_list = string.split(",")
        if not data_list[0] in data_dict:
            data_dict[data_list[0]] = int(data_list[1])
        else:
            data_dict[data_list[0]] += int(data_list[1])

    data.close()

    report = open(report_file_name, "w")
    report.write(
        f"supply,{data_dict['supply']}\n"
        f"buy,{data_dict['buy']}\n"
        f"result,{data_dict['supply'] - data_dict["buy"]}\n"
    )
    report.close()
