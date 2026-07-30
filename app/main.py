def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as f:
        elements = f.read().split()
        report_dict = {"supply": 0, "buy": 0, "result": 0}
        for elem in elements:
            key, value = elem.split(",")
            report_dict[key] += int(value)
        report_dict["result"] = report_dict["supply"] - report_dict["buy"]
        with open(report_file_name, "a") as w_file:
            for key, value in report_dict.items():
                w_file.write(f"{key},{value}\n")
