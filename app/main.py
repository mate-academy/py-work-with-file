def create_report(data_file_name: str, report_file_name: str) -> None:
    data_dict = {'supply': 0, 'buy': 0}
    with open(data_file_name, "r") as file:
        for line in file.readlines():
            key, value = line.split(",")
            value = int(value)
            data_dict[key] += value
    with open(report_file_name, "w") as file:
        file.write(f"supply,{data_dict['supply']}\n")
        file.write(f"buy,{data_dict['buy']}\n")
        file.write(f"result,{data_dict['supply'] - data_dict['buy']}\n")
