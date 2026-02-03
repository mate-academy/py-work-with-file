def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {
        "supply": 0,
        "buy": 0,
        "result": 0,
    }
    with open(data_file_name, "r") as file:
        for line in file.readlines():
            key, value = line.split(",")
            value = int(value)
            report[key] += value

    with open(report_file_name, "w") as file:
        file.write(f"supply,{report['supply']}\n")
        file.write(f"buy,{report['buy']}\n")
        file.write(f"result,{report['supply'] - report['buy']}\n")
