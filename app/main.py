def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as fr:
        with open(report_file_name, "w") as fw:
            text = fr.read()
            text = text.replace("\n", ",")
            items = text.split(",")
            report = {
                "supply": 0,
                "buy": 0
            }
            for index, operation in enumerate(items):
                if operation == "supply":
                    report["supply"] += int(items[index + 1])
                if operation == "buy":
                    report["buy"] += int(items[index + 1])
            report["result"] = report["supply"] - report["buy"]
            fw.write(
                f"supply,{report['supply']}\n"
                f"buy,{report['buy']}\n"
                f"result,{report['result']}\n"
            )
