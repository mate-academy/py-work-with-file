def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {"supply": 0,
              "buy": 0}
    with open(data_file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            split_line = line.split(",")
            name = split_line[0]
            if name == "supply":
                report["supply"] += int(split_line[1])
            elif name == "buy":
                report["buy"] += int(split_line[1])
        result = report["supply"] - report["buy"]
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{report['supply']}\n")
        report_file.write(f"buy,{report['buy']}\n")
        report_file.write(f"result,{result}\n")
