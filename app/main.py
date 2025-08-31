def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as input_file:
        for line in input_file:
            line = line.strip()
            if not line:
                continue
            operation, count = line.split(",")
            report[operation] += int(count)
    supply = report["supply"]
    buy = report["buy"]
    result = supply - buy
    with open(report_file_name, "w") as output_file:
        output_file.write(f"supply,{supply}\n")
        output_file.write(f"buy,{buy}\n")
        output_file.write(f"result,{result}\n")
    print(f"Report created: {report_file_name}")
