def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data,\
         open(report_file_name, "w") as report:
        data_dict = {}
        data_lines = data.readlines()
        lines = data_lines if data_lines[-1] else data_lines[:-1]
        for line in lines:
            key = line.split(",")[0]
            value = line.split(",")[1]
            data_dict[key] = data_dict.get(key, 0) + int(value)
        supply = f"supply,{data_dict.get('supply', 0)}\n"
        buy = f"buy,{data_dict.get('buy', 0)}\n"
        result = f"result," \
                 f"{data_dict.get('supply', 0) - data_dict.get('buy', 0)}\n"
        report.writelines([supply, buy, result])
