def create_report(data_file_name: str, report_file_name: str) -> None:

    with open(data_file_name, "r") as file:
        report_dict = {"buy": 0, "supply": 0}

        for line in file.read().split("\n"):
            if not line:
                break
            operation, amount = line.split(",")
            if operation == "buy":
                report_dict["buy"] += int(amount)
            if operation == "supply":
                report_dict["supply"] += int(amount)

    report_dict["result"] = report_dict["supply"] - report_dict["buy"]

    with open(report_file_name, "w") as report:
        output = (f"supply,{report_dict["supply"]}\nbuy,"
                  f"{report_dict["buy"]}\nresult,{report_dict["result"]}\n")
        report.write(output)
