
def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = dict()
    with open(f"../{data_file_name}", "r") as file:
        data = list(
            map(
                lambda value: {value.split(",")[0]: value.split(",")[1]},
                file.read().split("\n")[:-1]
            )
        )
        for log_dict in data:
            log_key = list(log_dict.keys())[0]
            log_value = list(log_dict.values())[0]
            if log_key in report_dict:
                report_dict[log_key] += int(log_value)
                continue
            report_dict[log_key] = int(log_value)
        report_dict["result"] = report_dict["supply"] - report_dict["buy"]
        with open(report_file_name, "w") as report_file:
            report_file.write("supply," + str(report_dict.get("supply")) + "\n")
            report_file.write("buy," + str(report_dict.get("buy")) + "\n")
            report_file.write("result," + str(report_dict.get("result")) + "\n")
