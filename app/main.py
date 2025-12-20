def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as csv_file:
        for line in csv_file:
            parts = line.split(",")
            if len(parts) < 2:
                continue

            operation = parts[0].strip()
            amount = int(parts[1].strip())
            if operation == "supply":
                supply += int(amount)
            elif operation == "buy":
                buy += int(amount)

    result = supply - buy

    report_content = f"supply,{supply}\nbuy,{buy}\nresult,{result}\n"

    with open(report_file_name, "w") as report_file:
        report_file.write(report_content)
