def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {"supply": 0, "buy": 0, "result": 0}

    with open(data_file_name, "r") as input_file:
        for line in input_file.readlines():
            operation, count = line.split(",")
            report[operation] += int(count)

    report["result"] = report["supply"] - report["buy"]
    supply = report["supply"]
    buy = report["buy"]
    result = report["result"]

    with (open(report_file_name, "a")
          as output_file):
        output_file.write(f"supply, {supply}\nbuy, {buy}\nresult, {result}\n")
