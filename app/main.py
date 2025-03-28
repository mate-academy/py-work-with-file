def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as data_file:
        data = data_file.readlines()
        for item in data:
            elem = item.split(",")
            report[elem[0]] += int(elem[1])

    with open(report_file_name, "a") as report_file:
        for key, item in report.items():
            report_file.write(f"{key},{item}\n")
        result = report["supply"] - report["buy"]
        report_file.write(f"result,{result}\n")
