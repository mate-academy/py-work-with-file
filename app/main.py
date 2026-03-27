def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as data_file:
        for row in data_file:
            key, item = row.rstrip("\n").split(",")
            report_dict[key] += int(item)
        report_dict.update(
            {"result": report_dict["supply"] - report_dict["buy"]}
        )
    supply = report_dict["supply"]
    buy = report_dict["buy"]
    result = report_dict["result"]
    with open(report_file_name, "w") as report_file:
        report_file.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{result}\n"
        )
