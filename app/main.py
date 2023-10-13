def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as data:
        for row in data.readlines():
            row_list = row.split(",")
            report_dict[row_list[0]] += int(row_list[1])

    with open(report_file_name, "w") as report:
        report.write(f"supply,{report_dict['supply']}\n"
                     f"buy,{report_dict['buy']}\n"
                     f"result,{report_dict['supply'] - report_dict['buy']}\n")
