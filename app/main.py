def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        data_list = data_file.readlines()

    new_data = {'supply': 0, 'buy': 0}
    for data in data_list:
        item = data.split(",")
        new_data[item[0]] += int(item[1].rstrip())

    with open(report_file_name, "w+") as report:
        report.write(f"supply,{new_data['supply']}\n")
        report.write(f"buy,{new_data['buy']}\n")
        report.write(f"result,{new_data['supply'] - new_data['buy']}\n")
