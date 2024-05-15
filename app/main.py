def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as data,
          open(report_file_name, "a") as report):
        report_dict = {}
        for line in data.readlines():
            action, number = line.split(",")
            report_dict[action] = int(report_dict.get(action, 0)) + int(number)
        report.write("supply" + "," + str(report_dict["supply"]) + "\n")
        report.write("buy" + "," + str(report_dict["buy"]) + "\n")
        report.write(
            "result" + ","
            + str(report_dict["supply"] - report_dict["buy"]) + "\n"
        )
