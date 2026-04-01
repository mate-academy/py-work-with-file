def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as source_file:
        data_base = source_file.read().split()

    data_dict = {}

    for data in data_base:
        key, value = data.split(",")
        if key not in data_dict:
            data_dict[key] = int(value)
        else:
            data_dict[key] += int(value)

    data_dict["result"] = int(data_dict["supply"]) - int(data_dict["buy"])

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{int(data_dict['supply'])}\n"
                          f"buy,{int(data_dict['buy'])}\n"
                          f"result,{str(data_dict['result'])}\n")
