def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as file:
        for line in file:
            key, value = line.strip().split(",")
            value = int(value)
            report_dict[key] += value

    report_dict["result"] = report_dict["supply"] - report_dict["buy"]

    with open(report_file_name, "w") as report_file:
        report_file.write(f'supply,{report_dict["supply"]}\n')
        report_file.write(f'buy,{report_dict["buy"]}\n')
        report_file.write(f'result,{report_dict["result"]}\n')
