def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {
        "supply": 0,
        "buy": 0,
        "result": 0,
    }
    with open(data_file_name) as file:
        for line in file.readlines():
            key, value = line.split(",")
            report_dict[key] += int(value)

    with open(report_file_name, "w") as file:
        file.write(f"supply,{report_dict['supply']}\n")
        file.write(f"buy,{report_dict['buy']}\n")
        file.write(f"result,{report_dict['supply'] - report_dict['buy']}\n")
