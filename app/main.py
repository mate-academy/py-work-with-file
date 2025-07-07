def create_report(
        data_file_name: str,
        report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name) as file:
        for line in file:
            if not line.strip():
                continue

            parts = line.split(",")
            if len(parts) != 2:
                continue

            operation = parts[0].strip().lower()
            try:
                amount = int(parts[1].strip())
            except ValueError:
                continue

            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\n")
        report.write(f"buy,{buy}\n")
        report.write(f"result,{supply - buy}\n")
