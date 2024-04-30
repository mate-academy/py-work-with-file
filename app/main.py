def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r")
          as file_in, open(report_file_name, "w") as file_out):
        report_data = {"supply": 0, "buy": 0}
        for line in file_in.readlines():
            split_line = line.split(",")
            report_data[split_line[0]] += int(split_line[1])
        file_out.write(
            f"supply, {report_data["supply"]}\n"
            f"buy, {report_data["buy"]}\n"
            f"result, {report_data["supply"] - report_data["buy"]}\n"
            .replace(" ", "")
        )
