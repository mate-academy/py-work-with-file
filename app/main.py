def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {"supply": 0, "buy": 0}
    with (open(data_file_name, "r") as data,
          open(report_file_name, "w") as report):

        for i in data.read().split():
            report_dict[i.split(",")[0]] += int(i.split(",")[1])

        report_content = (
            f"supply,{report_dict['supply']}\n"
            f"buy,{report_dict['buy']}\n"
            f"result,{report_dict['supply'] - report_dict['buy']}\n"
        )
        report.write(report_content)


create_report("oranges.csv", "oranges_report.csv")
