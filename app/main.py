def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as f:
        for line in f:
            operation, amount = line.strip().split(",")
            amount = int(amount)

            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount

    result = supply - buy

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
