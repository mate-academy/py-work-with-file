def create_report(data_file_name: str, report_file_name: str):
    report_dict = {}
    path = "../" + data_file_name
    data = open(path, "r")
    while True:
        line = data.readline()
        listed_line = line.strip().split(",")
        if not line:
            break
        if report_dict.get(listed_line[0]) is None:
            report_dict[listed_line[0]] = int(listed_line[1])
        else:
            report_dict[listed_line[0]] += int(listed_line[1])
    data.close()

    with open(report_file_name, "w") as report:
        report.write(f"supply,{report_dict['supply']}\n")
        report.write(f"buy,{report_dict['buy']}\n")
        report.write(f"result,"
                     f"{report_dict['supply'] - report_dict['buy']}\n")
