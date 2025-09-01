def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }
    with open(f"{data_file_name}", "r") as f:
        context = f.read()
        print(context)
        for line in context.split("\n"):
            print(line)
            values = line.split(",")
            if len(values) != 2:
                continue
            report[values[0]] += int(values[1])
        report["result"] = report["supply"] - report["buy"]

    result = ""
    for key in report:
        result += f"{key},{report[key]}\n"

    with open(f"{report_file_name}", "w") as f:
        print(result)
        f.write(result)
