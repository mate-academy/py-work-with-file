def create_report(data_file_name: str, report_file_name: str):
    file = open(data_file_name, "tr")
    res_dict = {}
    for line in file:
        list_of_words = line.split(",")
        if res_dict.get(list_of_words[0]) is None:
            res_dict[list_of_words[0]] = int(list_of_words[1])
        else:
            res_dict[list_of_words[0]] += int(list_of_words[1])
    file.close()
    res_dict["result"] = res_dict["supply"] - res_dict["buy"]

    report = open(report_file_name, "w")
    for key, value in res_dict.items():
        report.write(",".join((key, str(value))) + "\n")

    report.close()
