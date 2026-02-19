def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = buy = 0

    with open(data_file_name, "r", encoding="utf-8") as file:
        for line in file:
            operation, amount = line.split(",")
            if operation == "supply":
                supply += int(amount)
            elif operation == "buy":
                buy += int(amount)

    with open(report_file_name, "w", encoding="utf-8") as file:
        file.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
