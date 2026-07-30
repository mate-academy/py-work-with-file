def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as file:
        for line in file:
            operation, quantity = line.split(",")
            quantity = int(quantity)
            report_dict[operation] += quantity
    result = report_dict["supply"] - report_dict["buy"]
    report_dict["result"] = result
    with open(report_file_name, "w") as file:
        for key, value in report_dict.items():
            file.write(f"{key},{value}\n")
