def create_report(data_file_name: str,
                  report_file_name: str
                  ) -> str:
    data_file = open(data_file_name, "r")
    data_for_all = {"supply": 0, "buy": 0}
    for line in data_file.readlines():
        line_split = line.split(",")
        if len(line_split) == 2:
            if "supply" in line_split:
                data_for_all["supply"] += int(line_split[1])
            elif "buy" in line_split:
                data_for_all["buy"] += int(line_split[1])
    result = data_for_all["supply"] - data_for_all["buy"]
    report = open(report_file_name, "a")
    report.write("supply," + str(data_for_all["supply"]) + "\n")
    report.write("buy," + str(data_for_all["buy"]) + "\n")
    report.write("result," + str(result) + "\n")
    report.close()
    data_file.close()
