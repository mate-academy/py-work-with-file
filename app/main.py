def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        for line in file:
            clean_line = line.strip()

            if not clean_line:
                continue

            parts = clean_line.split(",")
            operation = parts[0]
            value = int(parts[1])

            if operation == "supply":
                supply += value
            elif operation == "buy":
                buy += value

    result = supply - buy

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\n")
        report.write(f"buy,{buy}\n")
        report.write(f"result,{result}\n")
