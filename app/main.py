def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            operation, amount = line.split(",")
            amount = int(amount)
            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount

    with open(report_file_name, "w") as fw:
        fw.write(f"supply,{supply}\n")
        fw.write(f"buy,{buy}\n")
        fw.write(f"result,{supply - buy}\n")