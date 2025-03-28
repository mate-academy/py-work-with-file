def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {
        "supply": 0,
        "buy": 0
    }

    with open(data_file_name, "r") as input_file:
        for line in input_file:
            current = line.split(",")
            if current[0] == "supply":
                report["supply"] += int(current[1])
            elif current[0] == "buy":
                report["buy"] += int(current[1])

    report["result"] = report["supply"] - report["buy"]

    with open(report_file_name, "w") as result_file:
        for key, value in report.items():
            result_file.write(f"{key},{str(value)}\n")
