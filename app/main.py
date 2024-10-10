def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    data_file_name = open(data_file_name, "r")
    report_file_name = open(report_file_name, "w")
    res_dict = {}
    for line in data_file_name.readlines():
        mn = line.split(",")
        if mn[0] not in res_dict:
            res_dict[mn[0]] = int(mn[1])
        else:
            res_dict[mn[0]] += int(mn[1])
    supply = res_dict["supply"]
    buy = res_dict["buy"]
    report_file_name.write(f"supply,{supply}\n"
                           f"buy, {buy}\n"
                           f"result, {supply - buy}")
    data_file_name.close()
    report_file_name.close()
