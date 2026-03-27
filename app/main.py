def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as data:
        data_list = data.read().replace(",", " ").split("\n")

    data_dict = {}
    for item in data_list:
        if item != "":
            item = item.split(" ")
            if item != "":
                if item[0] in data_dict:
                    data_dict[item[0]] += int(item[1])
                else:
                    data_dict[item[0]] = int(item[1])

    with open(report_file_name, "w") as report:
        report.writelines(f"supply,{data_dict['supply']}\n")
        report.writelines(f"buy,{data_dict['buy']}\n")
        report.writelines(f"result,{data_dict['supply'] - data_dict['buy']}\n")
