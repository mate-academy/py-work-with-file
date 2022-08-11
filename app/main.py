def create_report(data_file_name: str, report_file_name: str):
    report_dict = {"supply": 0, "buy": 0, "result": 0}
    with open(data_file_name, "r") as input_file,\
            open(report_file_name, "w") as output_file:
        for line in input_file:
            new_line = line.rstrip('\n').split(",")
            report_dict[new_line[0]] += int(new_line[1])
        report_dict["result"] = report_dict["supply"] - report_dict["buy"]
        output_file.write(f"supply,{report_dict['supply']}\n"
                          f"buy,{report_dict['buy']}\n"
                          f"result,{report_dict['result']}\n"
                          )
