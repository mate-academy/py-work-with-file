def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    report_dict = {"supply": 0, "buy": 0}

    for row in data_file:
        key, item = row.rstrip("\n").split(",")
        report_dict[key] += int(item)
    report_dict.update({"result": report_dict["supply"] - report_dict["buy"]})

    with open(report_file_name, "w") as report_file:
        report_file.write(
            f"supply,{report_dict["supply"]}\n"
            f"buy,{report_dict["buy"]}\n"
            f"result,{report_dict["result"]}\n"
        )
