def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    file = open(data_file_name, "r")
    for line in file:
        if not line.strip():
            continue

        operation, amount = line.strip().split(",")
        amount = int(amount)

        if operation == "supply":
            supply += amount
        else:
            buy += amount
    file.close()

    report = open(report_file_name, "w")
    report.write(f"supply,{supply}\n")
    report.write(f"buy,{buy}\n")
    report.write(f"result,{supply - buy}\n")
    report.close()