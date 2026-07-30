def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {}
    with open(data_file_name) as file:
        for line_full in file.readlines():
            line_list = line_full.strip().split(",")
            if line_list[0] not in report_dict:
                report_dict[line_list[0]] = int(line_list[1])
            else:
                report_dict[line_list[0]] += int(line_list[1])

    with open(report_file_name, "a") as file:
        file.write(f"supply,{report_dict['supply']}\n")
        file.write(f"buy,{report_dict['buy']}\n")
        file.write(f"result,{report_dict['supply'] - report_dict['buy']}\n")
