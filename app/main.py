def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    data_file_name = open(data_file_name, "r")
    filter_dict = {}
    for line in data_file_name.readlines():
        all_list = line.split(",")
        if all_list[0] not in filter_dict:
            filter_dict[all_list[0]] = int(all_list[1])
        else:
            filter_dict[all_list[0]] += int(all_list[1])
    supply = filter_dict["supply"]
    buy = filter_dict["buy"]
    result = supply - buy

    report_file_name = open(report_file_name, "w")
    report_file_name.write(f"supply,{supply}\n"
                           f"buy,{buy}\n"
                           f"result,{result}\n")

    data_file_name.close()
    report_file_name.close()
