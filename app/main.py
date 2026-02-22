def create_report(data_file_name: str, report_file_name: str) -> None:
    res = {}
    with open(data_file_name, "r") as data:
        content = data.readlines()
        for line in content:
            line = line.strip().split(",")
            if line[0] and line[0] not in res:
                res[line[0]] = int(line[1].strip())
            elif line[0]:
                res[line[0]] += int(line[1].strip())
            else:
                continue

    result = res["supply"] - res["buy"]
    supply = res["supply"]
    buy = res["buy"]

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\n")
        report.write(f"buy,{buy}\n")
        report.write(f"result,{result}\n")
