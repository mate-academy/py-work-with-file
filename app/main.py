def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.split(",")
            if line[0] == "supply":
                result["supply"] += int(line[1])
            elif line[0] == "buy":
                result["buy"] += int(line[1])
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{result['supply']}\n")
        report_file.write(f"buy,{result['buy']}\n")
        report_file.write(f"result,{result['supply'] - result['buy']}\n")
