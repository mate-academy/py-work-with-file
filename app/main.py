def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with open(data_file_name, "r") as data_file:
        data = data_file.readlines()
    result_dict = {}
    for line in data:
        key, value = line.split(",")
        result_dict[key] = result_dict.get(key, 0) + int(value)
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{result_dict['supply']}\n")
        report_file.write(f"buy,{result_dict['buy']}\n")
        report_file.write(f"result,"
                          f"{result_dict['supply'] - result_dict['buy']}\n")
