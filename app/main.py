def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as file:
        report_dict = {"supply": 0, "buy": 0, "result": 0}
        for line in file:
            key = line.split(",")[0]
            value = int(line.split(",")[1])
            report_dict[key] += value
        report_dict["result"] = report_dict['supply'] - report_dict['buy']
        with open(report_file_name, "w") as report:
            for key, value in report_dict.items():
                report.write(f"{key},{value}\n")
