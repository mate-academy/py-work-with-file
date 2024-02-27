def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with (open(data_file_name, "r") as input_file,
          open(report_file_name, "w") as report_file):
        report_data = {"supply": 0, "buy": 0}
        for row_data in input_file.readlines():
            key, val = row_data.split(",")
            report_data[key] += int(val)
        report_data["result"] = report_data["supply"] - report_data["buy"]

        for key, value in report_data.items():
            report_file.write(f"{key},{value}\n")
