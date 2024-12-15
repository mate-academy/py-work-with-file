def create_report(data_file_name: str, report_file_name: str) -> None:
    source_file = open(data_file_name)
    file_dict = {}

    for line in source_file:
        if len(line) > 0:
            line_list = line.rstrip("\n").split(",")
            if file_dict.get(line_list[0]) is None:
                file_dict[line_list[0]] = int(line_list[1])
            else:
                file_dict[line_list[0]] += int(line_list[1])

    file_dict["result"] = file_dict["supply"] - file_dict["buy"]

    report_file = open(report_file_name, "a")

    report_file.write(f"supply,{file_dict["supply"]}\n")
    report_file.write(f"buy,{file_dict["buy"]}\n")
    report_file.write(f"result,{file_dict["result"]}\n")

    source_file.close()
    report_file.close()
