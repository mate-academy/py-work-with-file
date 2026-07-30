def create_report(data_file_name: str, report_file_name: str) -> None:
    input_data = open(data_file_name, "r").readlines()
    input_data = [line.rstrip("\n") for line in input_data]
    report_data = {}
    for line in input_data:
        if report_data.get(line.split(",")[0]) is None:
            report_data[line.split(",")[0]] = int(line.split(",")[1])
        else:
            report_data[line.split(",")[0]] += int(line.split(",")[1])
    result = report_data["supply"] - report_data["buy"]
    report_data["result"] = result
    with open(report_file_name, "w") as file:
        file.write(f"supply,{report_data['supply']}\n")
        file.write(f"buy,{report_data['buy']}\n")
        file.write(f"result,{report_data['result']}\n")
