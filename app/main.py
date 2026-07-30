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
    report.write(",".join(("supply", str(res_dict["supply"]))) + "\n")
    report.write(",".join(("buy", str(res_dict["buy"]))) + "\n")
    report.write(",".join(("result", str(res_dict["result"]))) + "\n")

    report.close()
