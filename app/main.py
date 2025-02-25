def create_report(data_file_name: str, report_file_name: str) -> None:
    read_file = open(data_file_name, "r")
    report_file = open(report_file_name, "w")
    report = {}
    for string in read_file:
        string_split = string.split(",")
        string_split[1] = string_split[1][:-1]
        if string_split[0] not in report.keys():
            report[string_split[0]] = int(string_split[1])
        else:
            report[string_split[0]] += int(string_split[1])
    read_file.close()
    report["result"] = report["supply"] - report["buy"]
    report_file.write(f"supply,{report['supply']}\n")
    report_file.write(f"buy,{report['buy']}\n")
    report_file.write(f"result,{report['result']}\n")
    report_file.close()
