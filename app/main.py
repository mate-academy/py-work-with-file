def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as file:
        data = file.readlines()

    supply = 0
    buy = 0

    for row in data:
        operation, amount_str = row.strip().split(',')
        amount = int(amount_str)

        if operation == "supply":
            supply += amount
        elif operation == "buy":
            buy += amount

    result = supply - buy

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}")
