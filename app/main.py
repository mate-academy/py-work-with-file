def create_report(data_file_name:str, report_file_name:str) -> None:
    with open(data_file_name, "r") as data:
        list_data = data.read().splitlines()
    print(list_data)

    dict_data = {"supply": 0, "buy": 0}

    for data in list_data:
        part_data = data.split(",")
        if part_data[0] == "supply":
            dict_data["supply"] += int(part_data[1])
        if part_data[0] == "buy":
            dict_data["buy"] += int(part_data[1])

    with open(report_file_name, "w") as report:
        report.write(f"supply,{dict_data['supply']}\n")
        report.write(f"buy,{dict_data['buy']}\n")
        report.write(f"result,{dict_data['supply'] - dict_data['buy']}\n")
