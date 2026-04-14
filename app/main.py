def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as input_file:
        for line in input_file:
            operation, amount = line.strip().split(",")
            if operation in report_dict:
                report_dict[operation] += int(amount)
    report_dict["result"] = report_dict["supply"] - report_dict["buy"]

    with open(report_file_name, "w") as output_file:
        for key, value in report_dict.items():
            output_file.write(f"{key},{value}\n")
