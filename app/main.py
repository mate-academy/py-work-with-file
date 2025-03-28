def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {"supply": 0, "buy": 0}
    data_file = open(data_file_name, "r")
    for line in data_file.read().splitlines():
        operation, number = line.split(",")
        if operation == "buy":
            report_dict["buy"] += int(number)
        else:
            report_dict["supply"] += int(number)
    data_file.close()
    report_file = open(report_file_name, "w")
    for operation, number in report_dict.items():
        report_file.write(f"{operation},{number}\n")
    result = report_dict.get("supply") - report_dict.get("buy")
    report_file.write(f"result,{result}\n")
    report_file.close()
