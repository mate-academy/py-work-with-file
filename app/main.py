def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }
    with open(data_file_name, "r") as data_file:
        file_data = data_file.readlines()

    for line in file_data:
        operation, amount = line.strip().split(",")
        report[operation] += int(amount)
    report["result"] = report["supply"] - report["buy"]

    with open(report_file_name, "w") as report_file:
        report_file.write(
            f"supply,{report["supply"]}\n"
            f"buy,{report["buy"]}\n"
            f"result,{report["result"]}\n"
        )
