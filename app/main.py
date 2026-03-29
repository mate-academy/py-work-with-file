def create_report(data_file_name: str, report_file_name: str):
    result_dict = {}
    with open(data_file_name, "r") as input_file:
        for line in input_file.readlines():
            if len(line) > 0:
                new_line = line.split(",")
                if new_line[0] not in result_dict.keys():
                    result_dict[new_line[0]] = int(new_line[1])
                else:
                    result_dict[new_line[0]] += int(new_line[1])
    result_dict["result"] = result_dict["supply"] - result_dict["buy"]
    report = f"supply,{result_dict['supply']}\n" \
             f"buy,{result_dict['buy']}\n" \
             f"result,{result_dict['result']}\n"
    with open(report_file_name, "w") as report_file:
        report_file.write(report)
