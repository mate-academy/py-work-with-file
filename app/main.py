def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as r_file:
        result_dict = {}

        for line in r_file:
            line_list = line.rstrip("\n").split(",")
            if line_list[0] in result_dict:
                result_dict[line_list[0]] += int(line_list[1])
            else:
                result_dict[line_list[0]] = int(line_list[1])

    result_dict["result"] = result_dict["supply"] - result_dict["buy"]

    with open(report_file_name, "w") as w_file:
        for key, value in result_dict.items():
            w_file.write(f"{key},{value}\n")
