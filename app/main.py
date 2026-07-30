def create_report(data_file_name: str, report_file_name: str) -> None:
    my_dict = {}
    initial_file = open(data_file_name)
    for line in initial_file:
        pos = line.split(",")
        my_dict[pos[0]] = my_dict.get(pos[0], 0) + int(pos[1].strip())
    my_dict["result"] = my_dict["supply"] - my_dict["buy"]
    result = open(report_file_name, "w")
    result.write(
        f'supply,{my_dict["supply"]}\n'
        f'buy,{my_dict["buy"]}\n'
        f'result,{my_dict["result"]}\n'
    )
