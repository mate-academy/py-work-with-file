def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            if not line.strip():
                continue

            action, value = line.split(",")
            if action == "buy":
                result["buy"] += int(value)
            elif action == "supply":
                result["supply"] += int(value)

    report_line = (f"supply,{result['supply']}\n"
                   f"buy,{result['buy']}\n"
                   f"result,{result['supply'] - result['buy']}\n")

    with open(report_file_name, "w") as report:
        report.write(report_line)
