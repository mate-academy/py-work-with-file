def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    report_file = open(report_file_name, "w")

    report_dict = {
        "supply": 0,
        "buy": 0
    }

    for line in data_file:
        if not line:
            continue
        line_fields = line.split(",")
        if line_fields[0] == "supply":
            report_dict["supply"] += int(line_fields[1])
        elif line_fields[0] == "buy":
            report_dict["buy"] += int(line_fields[1])

    report_dict["result"] = report_dict["supply"] - report_dict["buy"]

    for operation_type, amount in report_dict.items():
        report_file.write(f"{operation_type},{amount}\n")

    data_file.close()
    report_file.close()
