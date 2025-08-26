def create_report(
    data_file_name: str,
    report_file_name: str
) -> None:
    data_file = open(data_file_name, "r")
    results = {
        "buy": 0,
        "supply": 0,
        "result": 0
    }
    for data_line in data_file:
        if data_line == "":
            break
        service, value = data_line.split(",")
        value = int(value)
        results[service] += value

    data_file.close()
    results["result"] = results["supply"] - results["buy"]

    report_file = open(report_file_name, "w")

    report_file.write(f"supply,{results["supply"]}\n")
    report_file.write(f"buy,{results["buy"]}\n")
    report_file.write(f"result,{results["result"]}\n")

    report_file.close()
