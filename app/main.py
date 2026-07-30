def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    result_dict = {}

    with open(data_file_name, "r") as data:
        for line in data.readlines():
            value = line.split(",")
            result_dict[value[0]] = result_dict.get(value[0], 0) \
                + int(value[1])
    with open(report_file_name, "w") as report:
        report.write(f"supply,{result_dict['supply']}\n"
                     f"buy,{result_dict['buy']}\n"
                     f"result,{result_dict['supply'] - result_dict['buy']}\n")
