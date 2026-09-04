def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            if line == "\n":
                continue

            operation, amount = line.strip().split(",")
            amount = int(amount.replace("\n", ""))

            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount
    result = supply - buy
    data_file.close()
    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\n")
        f.write(f"buy,{buy}\n")
        f.write(f"result,{result}\n")
