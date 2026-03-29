def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with (
        open(data_file_name, "r") as file_in,
        open(report_file_name, "w") as file_out
    ):
        report = {
            "supply": 0,
            "buy": 0
        }
        for line in file_in.readlines():
            operation, amount = line.split(",")
            report[operation] += int(amount)
        report["result"] = report["supply"] - report["buy"]

        for key, value in report.items():
            file_out.writelines(f"{key},{value}\n")
