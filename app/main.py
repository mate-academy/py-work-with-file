def create_report(data_file_name: str, report_file_name: str) -> None:
    data = {}
    with open(data_file_name, "r") as d:
        for line in d:
            if not line.strip():
                continue

            key, value = line.strip().split(",")
            data[key] = data.get(key, 0) + int(value)

    supply = data.get("supply", 0)
    buy = data.get("buy", 0)
    result = supply - buy

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\n")
        report.write(f"buy,{buy}\n")
        report.write(f"result,{result}\n")
