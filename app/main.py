def create_report(data_file_name: str, report_file_name: str) -> None:
    working_file = open(data_file_name, "r")
    result = {"supply": 0, "buy": 0, "result": 0}

    for line in working_file:
        if "supply" in line:
            result["supply"] += int(line.split(",")[1])
        elif "buy" in line:
            result["buy"] += int(line.split(",")[1])
    result["result"] = result["supply"] - result["buy"]
    for key, value in result.items():
        with open(report_file_name, "a") as report:
            report.write(f"{key},{value}\n")

    working_file.close()
