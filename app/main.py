def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    delta_dict = {}

    with open(data_file_name, "r") as data:
        for line in data.readlines():
            value = line.split(",")
            delta_dict[value[0]] = delta_dict.get(value[0], 0) + int(value[1])
    with open(report_file_name, "w") as report:
        report.write(f"supply,{delta_dict['supply']}\n"
                     f"buy,{delta_dict['buy']}\n"
                     f"result,{delta_dict['supply'] - delta_dict['buy']}\n")
