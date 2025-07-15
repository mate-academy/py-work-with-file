def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {}
    with open(f"../{data_file_name}", "r") as file:
        lines = file.readlines()
        cleaned = [line.strip() for line in lines]
        for i in cleaned:
            key, val = i.split(",")
            report[key] = report.get(key, 0) + int(val)
    report["result"] = report.get("supply", 0) - report.get("buy", 0)
    ordered_keys = ["supply", "buy", "result"]
    result = "\n".join(f"{key},{report.get(key, 0)}"
                       for key in ordered_keys if key in report)
    result = result + "\n"
    with open(report_file_name, "w") as file_2:
        file_2.write(result)
