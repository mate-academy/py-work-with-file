def create_report(data_file_name: str, report_file_name: str) -> None:

    data = open(data_file_name, "r")

    report_dict = {"supply": 0, "buy": 0}

    for row in data:
        if not row.strip():
            continue
        key = row.split(",")[0]
        value = int(row.split(",")[1])
        if key not in report_dict:
            report_dict[key] = value
        else:
            report_dict[key] += value
    data.close()

    output = open(report_file_name, "w")
    result = report_dict["supply"] - report_dict["buy"]

    output.write("supply" + "," + str(report_dict["supply"]) + "\n"
                 + "buy" + "," + str(report_dict["buy"]) + "\n"
                 + "result" + "," + str(result) + "\n")
    output.close()
