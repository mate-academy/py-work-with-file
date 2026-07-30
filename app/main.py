def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with open(data_file_name, "r") as data_file:
        list1 = [line.rstrip().split(",") for line in data_file.readlines()]

    dict1 = {}
    for inner_list in list1:
        if inner_list[0] not in dict1:
            dict1[inner_list[0]] = int(inner_list[1])
        else:
            dict1[inner_list[0]] += int(inner_list[1])

    with open(f"{report_file_name}", "a") as report:
        report.write(f"supply,{dict1['supply']}\n")
        report.write(f"buy,{dict1['buy']}\n")
        report.write(f"result,{dict1['supply'] - dict1['buy']}\n")
