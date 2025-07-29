def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        report = {
            "supply":0,
            "buy":0,
            "result":0
        }
        for line in file:
            key = line.strip().split(",")[0]
            value = line.strip().split(",")[1]
            report[key] += int(value)
        report["result"] = report["supply"] - report["buy"]
    with open(report_file_name,"a") as file:
        for k,v in report.items():
            file.write(f"{k},{v}\n")

