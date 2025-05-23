def create_report(
    data_file_name: str,
    report_file_name: str
) -> None:
    data_file = open(data_file_name, "r")
    report_file = open(report_file_name, "w")
    report_dict = {"supply": 0, "buy": 0}

    for line in data_file:
        line = line.strip()
        if not line:
            continue
        key, value = line.split(",")
        report_dict[key] += int(value)

    result = report_dict["supply"] - report_dict["buy"]
    report_dict["result"] = result

    for key, value in report_dict.items():
        report_file.write(f"{key},{value}\n")

    data_file.close()
    report_file.close()
