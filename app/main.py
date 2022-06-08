def create_report(data_file_name: str, report_file_name: str):
    for_reading = open(data_file_name, 'r')
    # with open(report_file_name, 'w+') as for_writing:
    my_dict = {}
    for row in for_reading:
        line = row.split(",")
        if str(line[0]) not in my_dict:
            my_dict[str(line[0])] = int(line[1])
        else:
            my_dict[str(line[0])] += int(line[1])
    my_dict["result"] = my_dict["supply"] - my_dict["buy"]
    with open(report_file_name, 'w+') as for_writing:
        # for_writing.write(my_dict)
        for_writing.write(f"supply,{my_dict['supply']}\n")
        for_writing.write(f"buy,{my_dict['buy']}\n")
        for_writing.write(f"result,{my_dict['result']}\n")
