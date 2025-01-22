def create_report(data_file_name: str, report_file_name: str) -> None:
    data_dict = {}
    data_file = open(data_file_name)
    for row in data_file:
        key, value = row.split(",")
        if key not in data_dict:
            data_dict[key] = int(value)
        else:
            data_dict[key] += int(value)
        print(data_dict)
    data_file.close()
    report_file = open(report_file_name, mode="a")
    report_file.write(f"supply,{data_dict["supply"]}\n")
    report_file.write(f"buy,{data_dict["buy"]}\n")
    result = data_dict["supply"] - data_dict["buy"]
    report_file.write(f"result,{result}\n")
    report_file.close()
