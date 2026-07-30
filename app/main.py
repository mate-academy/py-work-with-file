def create_report(data_file_name: str, report_file_name: str) -> None:
    file_csv = open(data_file_name)
    supply = 0
    buy = 0
    for line in file_csv:
        line = line.strip()
        operation, amount = line.split(",")
        if operation == "supply":
            supply += int(amount)
        if operation == "buy":
            buy += int(amount)
    file_csv.close()

    with open(report_file_name, "w", encoding="utf-8") as file:
        file.write(f"supply,{supply}\n")
        file.write(f"buy,{buy}\n")
        file.write(f"result,{supply - buy}\n")
