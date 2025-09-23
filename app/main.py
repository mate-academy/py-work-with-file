def create_report(data_file_name: str, report_file_name: str) -> None:
    file_name = open(data_file_name, "r")
    res_dict = {}
    for line in file_name:
        list_of_words = line.split(",")
        if res_dict.get(list_of_words[0]) is None:
            res_dict[list_of_words[0]] = int(list_of_words[1])
        else:
            res_dict[list_of_words[0]] += int(list_of_words[1])
    file_name.close()
    res_dict["result"] = res_dict["supply"] - res_dict["buy"]

    report = open(report_file_name, "w")
    for key, value in res_dict.items():
        report.write(",".join((key, str(value))) + "\n")

    report.close()
