def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")

    result_dict = {
        "supply": 0,
        "buy": 0,
    }

    for line in data_file.readlines():
        line = line.split(",")
        if line[0] == "supply":
            result_dict["supply"] += int(line[1])
        if line[0] == "buy":
            result_dict["buy"] += int(line[1])

    result_dict["result"] = result_dict["supply"] - result_dict["buy"]

    report = open(report_file_name, "w")
    report.write(
        f"supply,{result_dict['supply']}\n"
        f"buy,{result_dict['buy']}\n"
        f"result,{result_dict['result']}\n"
    )

    data_file.close()
    report.close()
