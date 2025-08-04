def create_report(data_file_name: str, report_file_name: str) -> None:
    operations = {
        "supply": 0,
        "buy": 0,
    }
    data = open(data_file_name, "r")
    for line in data:
        if line:
            key, value = line.split(",")
            operations[key] += int(value)
    data.close()
    report = open(report_file_name, "a")
    for key, value in operations.items():
        report.write(f"{key},{value}\n")
    supply = operations["supply"]
    buy = operations["buy"]
    report.write(f"result,{supply - buy}\n")
    report.close()
