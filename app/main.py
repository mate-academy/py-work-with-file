def create_report(data_file_name: str, report_file_name: str) -> None:
    file_of_inf = open(data_file_name)
    dict_of_inf = {}
    for item in file_of_inf.readlines():
        line_list = item.split(",")
        if line_list[0] not in dict_of_inf:
            dict_of_inf[line_list[0]] = int(line_list[1])
        else:
            dict_of_inf[line_list[0]] += int(line_list[1])

    file_of_inf.close()

    dict_of_inf["result"] = dict_of_inf.get("supply") - dict_of_inf.get("buy")

    new_report = open(report_file_name, "w")

    for key in ["supply", "buy", "result"]:  # порядок гарантовано правильний
        if key in dict_of_inf:
            new_report.write(f"{key},{dict_of_inf[key]}\n")

    new_report.close()
