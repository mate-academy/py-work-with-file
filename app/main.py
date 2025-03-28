def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_count = 0
    buy_count = 0
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):
        report_list = file_in.readlines()
        for report in report_list:
            text_report = report.split(",")[0]
            count_report = int(report.split(",")[1])
            if text_report == "supply":
                supply_count += count_report
            elif text_report == "buy":
                buy_count += count_report
        file_out.write(f"supply,{supply_count}\n"
                       f"buy,{buy_count}\n"
                       f"result,{supply_count - buy_count}\n")
