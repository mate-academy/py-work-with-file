def create_report(data_file_name: str, report_file_name: str) -> None:
    report_data = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }
    with open(data_file_name, "r") as read_file:
        for line in read_file:
            name, number = line.split(",")
            if name in report_data:
                report_data[name] += int(number)
    report_data["result"] = report_data["supply"] - report_data["buy"]
    with open(report_file_name, "w") as save_file:
        for key, value in report_data.items():
            save_file.write(f"{key},{value}\n")
