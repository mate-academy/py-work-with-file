def create_report(data_from_file: str,
                  report_file_name: str) -> None:
    supply = 0
    buy = 0
    start_file = open(data_from_file)
    start_file = open(data_from_file)
    for line in start_file:
        if not line.strip():
            continue
        operation, amount = line.split(",")
        amount = int(amount)
        if operation == "supply":
            supply += amount
        elif operation == "buy":
            buy += amount
    start_file.close()
    report = open(report_file_name, "w")
    report.write(f"supply,{supply}\n")
    report.write(f"buy,{buy}\n")
    report.write(f"result,{supply - buy}\n")
    report.close()
