def create_report(data_file_name: str, report_file_name: str):
    supply = 0
    buy = 0

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.strip()
            if line:
                operation, amount = line.split(",")
                amount = int(amount)
                if operation == "supply":
                    supply += amount
                elif operation == "buy":
                    buy += amount
    result = supply - buy
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")