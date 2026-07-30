def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as file_in:
        report = {}
        lines = file_in.read().replace("\\n", " ").split()

        for line in lines:
            key, value = line.split(",")
            if key not in report:
                report[key] = int(value)
            else:
                report[key] += int(value)

        report["result"] = report["supply"] - report["buy"]
        report_str = f"supply,{report['supply']}\nbuy," \
                     f"{report['buy']}\nresult,{report['result']}\n"

    with open(report_file_name, "w") as file_out:
        file_out.write(report_str)
