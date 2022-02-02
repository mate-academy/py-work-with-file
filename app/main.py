def create_report(data_file_name: str, report_file_name):
    report_dict = {"buy": 0, "supply": 0}
    with open(data_file_name) as source:
        for line in source:
            info = line.strip('\n').split(',')
            report_dict[info[0]] += int(info[1])
        report_dict["rest"] = report_dict["supply"] - report_dict["buy"]
        with open(report_file_name, "w") as report:
            report.write("supply,{supply}\nbuy,{buy}\nresult,{rest}\n".format(**report_dict))
