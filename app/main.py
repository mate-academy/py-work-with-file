def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with (
        open(data_file_name, "r") as data,
        open(report_file_name, "w") as report
    ):
        summary = {"supply": 0, "buy": 0}
        for line in data.readlines():
            list_from_line = line.split(",")
            dict_from_list = {list_from_line[0]: int(list_from_line[1])}
            summary[list_from_line[0]] += dict_from_list[list_from_line[0]]
        report.write(
            f"supply,{summary['supply']}\n"
            f"buy,{summary['buy']}\n"
            f"result,{summary['supply'] - summary['buy']}\n"
        )
