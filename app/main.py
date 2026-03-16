def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    data = open(data_file_name)
    report_dict = {"supply": 0, "buy": 0}
    for line in data:
        splitted = line[:-1].split(",")
        report_dict[splitted[0]] += int(splitted[1])
    data.close()
    report_dict["result"] = report_dict["supply"] - report_dict["buy"]
    output_string = \
        (f'supply,{report_dict["supply"]}\n'
         f'buy,{report_dict["buy"]}\n'
         f'result,{report_dict["result"]}\n')
    output_f = open(report_file_name, "w")
    output_f.write(output_string)
    output_f.close()
