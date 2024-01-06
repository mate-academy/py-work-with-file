def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    report = {"supply": 0, "buy": 0, "result": 0}
    with open(data_file_name, "r") as file_in:
        content = file_in.readlines()

        for i in range(len(content)):
            item = content[i].split(",")
            if item[0] == "supply":
                report[item[0]] += int(item[1].strip())
            if item[0] == "buy":
                report[item[0]] += int(item[1].strip())
    report["result"] = report["supply"] - report["buy"]

    with open(report_file_name, "w") as file_out:
        for key, value in report.items():
            file_out.write(f"{key},{value}\n")
