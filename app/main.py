def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {
        "supply": 0,
        "buy": 0
    }

    with open(data_file_name, "r") as file:
        text = file.read()
        text = text.replace("\n", ",")
        items = text.split(",")
        for index, operation in enumerate(items):
            if operation == "supply":
                report["supply"] += int(items[index + 1])
            if operation == "buy":
                report["buy"] += int(items[index + 1])
        report["result"] = report["supply"] - report["buy"]

    with open(report_file_name, "w") as file:
        file.write(
            f"supply,{report['supply']}\n"
            f"buy,{report['buy']}\n"
            f"result,{report['result']}\n"
        )
