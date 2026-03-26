def create_report(data_file_name: str, report_file_name: str) -> None:
    csv_contents = open(data_file_name)
    lines = csv_contents.readlines()
    report_dict = {}
    report = ""

    for i in range(1, len(lines)):
        key, value = lines[i].split(",")
        if key in report_dict:
            report_dict[key] += int(value)
        else:
            report_dict[key] = int(value)
    csv_contents.close()
    for key, value in report_dict.items():
        report += f"{key},{value}\n"
    report_list = list(report_dict.values())
    report += f"result,{report_list[0] - report_list[1]}"
    output = open(report_file_name, "w")
    output.write(report)
    output.close()
