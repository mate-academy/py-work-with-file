def create_report(data_file_name: str, report_file_name: str) -> None:
    result = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }
    with open(data_file_name) as data_file:
        for line in data_file:
            changed = line.replace("\n", "").split(",")
            if "buy" in changed:
                result["buy"] += int(changed[1])
            elif "supply" in changed:
                result["supply"] += int(changed[1])
    result["result"] = result["supply"] - result["buy"]
    with open(report_file_name, "a") as report_file:
        for key, value in result.items():
            report_file.write(f"{key},{value}\n")
