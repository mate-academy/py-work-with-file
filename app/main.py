def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    data_file = open(data_file_name, "r")
    for line in data_file:
        if not line.strip():
            continue
        operation, amount = line.strip().split(",")
        if operation == "supply":
            supply += int(amount)
        if operation == "buy":
            buy += int(amount)
    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
    data_file.close()
    report_file.close()
