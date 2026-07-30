def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    report_dict = {"supply": 0,
                   "buy": 0}
    with (open(data_file_name, "r") as original,
          open(report_file_name, "a") as report):
        for line in original.readlines():
            parts_of_line = line.replace("\n", "").split(",")
            report_dict[parts_of_line[0]] += int(parts_of_line[1])
        report_dict["result"] = report_dict["supply"] - report_dict["buy"]
        for key, value in report_dict.items():
            report.write(f"{key},{value}\n")
