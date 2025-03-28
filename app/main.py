def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        data = file.readlines()
    supply = 0
    buy = 0
    for line in data:
        operation, amount = line.strip().split(",")
        if operation == "supply":
            supply += int(amount)
        elif operation == "buy":
            buy += int(amount)
    result = supply - buy
    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
