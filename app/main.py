def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as data,
          open(report_file_name, "w") as report):
        report_dict = dict()
        for line_data in data.readlines():
            if line_data.count(",") > 0:
                line_key, line_value = line_data.split(",")
                if line_key in report_dict.keys():
                    report_dict[line_key] = \
                        report_dict.get(line_key) \
                        + int(line_value)
                else:
                    if len(line_key) > 0 and len(line_value) > 0:
                        report_dict.setdefault(line_key, int(line_value))
        result = report_dict["supply"] - report_dict["buy"]
        report.write("supply," + str(report_dict["supply"]) + "\n")
        report.write("buy," + str(report_dict["buy"]) + "\n")
        report.write("result," + str(result) + "\n")


if __name__ == "__main__":
    create_report("../bananas.csv", "../bananas_report.csv")
