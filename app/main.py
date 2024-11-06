def create_report(data_file_name: str, report_file_name: str) -> None:

    data_file = open(data_file_name, "r")

    result_dict = {"supply": 0, "buy": 0}

    for line in data_file.readlines():
        if "supply" in line.split(",")[0]:
            key = "supply"
        else:
            key = "buy"
        result_dict[key] += int(line.split(",")[1])
    data_file.close()

    result_dict["result"] = result_dict["supply"] - result_dict["buy"]

    result_file = open(report_file_name, "w")

    result_file.write("supply,{}\n".format(result_dict["supply"]))
    result_file.write("buy,{}\n".format(result_dict["buy"]))
    result_file.write("result,{}\n".format(result_dict["result"]))

    result_file.close()
