def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as file, \
         open(report_file_name, "w") as report:
        text = file.read()

        report_dict = {
            "supply": 0,
            "buy": 0,
            "result": 0,
        }
        for element in text.split("\n"):
            if element != "":
                key = element.split(",")[0]
                value = int(element.split(",")[1])
                report_dict[key] += value

        report_dict["result"] = report_dict["supply"] - report_dict["buy"]

        for key, value in report_dict.items():
            report.write(f"{key},{value}\n")
