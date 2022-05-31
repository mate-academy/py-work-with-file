def create_report(data_file_name: str, report_file_name: str):
    data_dict = {}
    with open(data_file_name, "r") as file:
        content = file.readlines()
        for line in content:
            name = line.split(",")[0]
            value = line.split(",")[1]
            if name in data_dict:
                data_dict[name] += int(value)
            else:
                data_dict[name] = int(value)
    report = [
        f'supply,{data_dict["supply"]}\n',
        f'buy,{data_dict["buy"]}\n',
        f'result,{data_dict["supply"] - data_dict["buy"]}\n'
    ]
    with open(report_file_name, "w") as file:
        file.writelines(report)
