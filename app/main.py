def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    report_dict = {"supply": 0,
                   "buy": 0,
                   "result": 0
                   }
    with open(data_file_name, "r") as file:
        for line in file:
            operation, amount_str = line.strip().split(",")
            amount = int(amount_str)
            if operation == "buy":
                report_dict["buy"] += amount
            elif operation == "supply":
                report_dict["supply"] += amount

    report_dict["result"] = report_dict["supply"] - report_dict["buy"]

    with open(report_file_name, "w") as file_report:
        for key, value in report_dict.items():
            file_report.write(f"{key},{value}\n")
