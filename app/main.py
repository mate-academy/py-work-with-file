def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as source:
        result = {"supply": 0, "buy": 0}
        for line in source.readlines():
            result[line.split(",")[0]] += int(line.split(",")[1])

    with open(report_file_name, "w") as report:
        difference = result['supply'] - result['buy']
        report.write(f"supply,{result['supply']}\n"
                     f"buy,{result['buy']}\n"
                     f"result,{difference}\n")
