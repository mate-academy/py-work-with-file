def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, 'r') as data_file:
        lines = data_file.readlines()

    dict_data = {}
    for line in lines:
        name, amount = line.split(',')
        if name in dict_data:
            dict_data[name] += int(amount)
        else:
            dict_data[name] = int(amount)
    dict_data["result"] = dict_data["supply"] - dict_data["buy"]

    with open(report_file_name, 'w') as report_file:
        report_file.write(f"supply,{dict_data['supply']}\n")
        report_file.write(f"buy,{dict_data['buy']}\n")
        report_file.write(f"result,{dict_data['result']}\n")
