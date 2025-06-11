def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {"supply": 0, "buy": 0}
    file = open(data_file_name, "r")
    for i in file:
        line = i.strip()
        if not line:
            continue
        file_split = line.split(",")
        if file_split[0] == "supply":
            result["supply"] += int(file_split[1])
        if file_split[0] == "buy":
            result["buy"] += int(file_split[1])
    file.close()
    result_minus = result["supply"] - result["buy"]
    file_report = open(report_file_name, "w")
    file_report.write(f"supply,{result['supply']}\n"
                      f"buy,{result['buy']}\n"
                      f"result,{result_minus}\n")
    file_report.close()
