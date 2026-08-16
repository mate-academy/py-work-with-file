

def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as data:
        data_list = [line.strip().split(",") for line in data]
    report_dict = {}
    for data in data_list:
        report_dict[data[0]] = report_dict.get(data[0], 0) + int(data[1])
    report_list = [
        f"supply,{report_dict['supply']}",
        f"buy,{report_dict['buy']}",
        f"result,{report_dict['supply'] - report_dict['buy']}"
    ]
    with open(report_file_name, "w") as report:
        report.write("\n".join(report_list) + "\n")
