def create_report(data_file_name: str, report_file_name: str) -> None:

    result = []

    with open(data_file_name, "r") as info:
        for line in info.readlines():
            result.append(line.strip().split(","))

    result2 = {}

    for i in result:
        if i[0] not in result2:
            result2[i[0]] = int(i[1])
        else:
            result2[i[0]] += int(i[1])

    with open(report_file_name, "a") as report:
        report.write(f"supply,{result2['supply']}\n")
        report.write(f"buy,{result2['buy']}\n")
        report.write(f"result,{result2['supply'] - result2['buy']}\n")
