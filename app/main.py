def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    result = 0
    with open(data_file_name, "r", encoding="utf-8") as data_source:
        for line in data_source:
            stripped = line.strip()
            if not stripped:
                continue

            data = stripped.split(",")

            if len(data) != 2:
                continue

            amount = int(data[1])

            if data[0] == "supply":
                supply += amount
            elif data[0] == "buy":
                buy += amount

    result = supply - buy

    with open(report_file_name, "w", encoding="utf-8") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{result}\n")
