def create_report(data_file_name: str, report_file_name: str) -> None:
    data = open(data_file_name, "r")
    report_dict = {}
    for line in data.readlines():
        action, value = line.rstrip("\n").split(",")
        if action in report_dict:
            report_dict[action] += int(value)
            continue
        report_dict[action] = int(value)
    report_dict["result"] = report_dict["supply"] - report_dict["buy"]
    data.close()
    report_str = ("supply" + "," + f"{report_dict["supply"]}\nbuy" + ","
                  + f"{report_dict["buy"]}\nresult" + ","
                  + f"{report_dict["result"]}\n")
    report_file = open(report_file_name, "w")
    report_file.write(report_str)
    report_file.close()
