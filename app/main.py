def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {}
    file_data = open(data_file_name, "r")
    for line in file_data:
        line = line.strip()
        if not line:
            continue
        name, value = line.split(",")
        value = int(value)
        report_dict[name] = report_dict.get(name, 0) + value
    file_data.close()
    report_dict["result"] = (
        report_dict.get("supply", 0) - report_dict.get("buy", 0)
    )
    file_report = open(report_file_name, "w")
    file_report.write(
        f"supply,{report_dict['supply']}\n"
        f"buy,{report_dict['buy']}\n"
        f"result,{report_dict['result']}\n"
    )
    file_report.close()
