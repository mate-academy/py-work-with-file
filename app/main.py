def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(f"{data_file_name}", "r") as data_file:
        strings = data_file.readlines()

    data_dict = {}
    for string in strings:
        [key, value] = string.split(",")
        if key not in data_dict:
            data_dict[key] = int(value)
        else:
            data_dict[key] += int(value)

    with open(f"{report_file_name}", "a") as report_file:
        report_file.write(f"supply,{data_dict['supply']}\n")
        report_file.write(f"buy,{data_dict['buy']}\n")
        report_file.write(f"result,{data_dict['supply'] - data_dict['buy']}\n")
