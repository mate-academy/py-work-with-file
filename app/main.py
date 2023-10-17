def create_report(data_file_name: str, report_file_name: str) -> None:

    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):

        report = {
            "supply": 0,
            "buy": 0,
            "result": 0
        }

        for line in data_file:
            if "supply" in line:
                supply_value = int(line.split(",")[1])
                report["supply"] += supply_value
            elif "buy" in line:
                buy_value = int(line.split(",")[1])
                report["buy"] += buy_value

        report["result"] = report["supply"] - report["buy"]
        report_to_file = (f"supply,{report['supply']}\n"
                          f"buy,{report['buy']}\nresult,{report['result']}\n")

        report_file.writelines(report_to_file)
