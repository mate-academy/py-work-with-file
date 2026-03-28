def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as fin:
        report = {
            "supply": 0,
            "buy": 0,
            "result": 0
        }

        for line in fin.readlines():
            splited_line = line.split(",")
            report[splited_line[0]] += int(splited_line[1])

        report["result"] = report["supply"] - report["buy"]

    with open(report_file_name, "w") as fout:
        for operation, amount in report.items():
            fout.write(f"{operation},{amount}\n")
