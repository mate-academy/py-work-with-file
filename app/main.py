def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as f:
        for line in f.readlines():
            if line == "":
                continue
            if line.split(",")[0] == "supply":
                result["supply"] += int(line.split(",")[1])
            elif line.split(",")[0] == "buy":
                result["buy"] += int(line.split(",")[1])
    with open(report_file_name, "w") as f:
        f.write(f"supply,{result['supply']}\n"
                f"buy,{result['buy']}\n"
                f"result,{result['supply'] - result['buy']}\n")
