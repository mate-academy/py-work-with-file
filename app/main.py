def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {
        "supply": 0,
        "buy": 0,
    }

    with open(data_file_name) as file_name:
        for actions in file_name:
            action = actions.strip().split(",")
            if action[0] == "supply":
                report_dict["supply"] += int(action[1])
            else:
                report_dict["buy"] += int(action[1])

    report_dict["result"] = report_dict["supply"] - report_dict["buy"]

    with open(report_file_name, "w") as report:
        for key, value in report_dict.items():
            report.write(f"{key},{value}\n")
