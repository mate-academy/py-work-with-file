def create_report(data_file_name: str, report_file_name: str) -> None:
    dict_report = {}
    with open(data_file_name, "r") as file:
        for line in file:
            list_line = line.strip().split(",")
            if list_line[0] in dict_report:
                dict_report[list_line[0]] += int(list_line[1])
            else:
                dict_report[list_line[0]] = int(list_line[1])
    count_supply = dict_report["supply"]
    count_buy = dict_report["buy"]
    with open(report_file_name, "w") as file:
        file.write(f"supply,{count_supply}\n")
        file.write(f"buy,{count_buy}\n")
        file.write(f"result,{count_supply - count_buy}\n")
