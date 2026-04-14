def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    report_file = open(report_file_name, "w")

    data = {}

    for line in data_file:
        line = line.split(",")
        if line[0] not in data:
            data[line[0]] = int(line[1].strip("\n"))
        else:
            data[line[0]] += int(line[1].strip("\n"))

    report_file.write(f"supply,{data['supply']}\n")
    report_file.write(f"buy,{data['buy']}\n")
    report_file.write(f'result,{data["supply"] - data["buy"]}\n')

    data_file.close()
    report_file.close()
