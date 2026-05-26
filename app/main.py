def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")

    new_dict = {}
    for line in data_file:
        line_list = line.strip().split(",")
        if line_list[0] not in new_dict:
            new_dict[line_list[0]] = int(line_list[1])
        else:
            new_dict[line_list[0]] += int(line_list[1])

    data_file.close()

    result = new_dict["supply"] - new_dict["buy"]
    new_dict["result"] = result

    raport = open(report_file_name, "w")

    raport.write(f'supply,{new_dict["supply"]}\n')
    raport.write(f'buy,{new_dict["buy"]}\n')
    raport.write(f'result,{new_dict["result"]}\n')

    raport.close()
