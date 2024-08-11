def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as f_data:
        supply = 0
        buy = 0
        for line in f_data:
            line_data = line.split(",")
            if line_data[0] == "supply":
                supply += int(line_data[1].rstrip("\n"))
            if line_data[0] == "buy":
                buy += int(line_data[1].rstrip("\n"))

    with open(report_file_name, "w") as f_report:
        f_report.write(",".join(("supply", f"{supply}\nbuy",
                                 f"{buy}\nresult",
                                 f"{supply - buy}\n")))
