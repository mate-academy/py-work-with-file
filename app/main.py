def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as data_file:
        line_list = [line.replace("\n", "").split(",") for line in data_file]
        report = {"supply": 0, "buy": 0}
        for item, number in line_list:
            report[item] += int(number)
        report["result"] = report["supply"] - report["buy"]
        with open(report_file_name, "w") as report_file:
            report_file.write(
                f"supply,{report['supply']}\n"
                f"buy,{report['buy']}\n"
                f"result,{report['result']}\n"
            )
