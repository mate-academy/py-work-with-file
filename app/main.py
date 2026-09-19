def create_report(data_file_name: str, report_file_name: str) -> None:
    buy = 0
    supply = 0
    with open(data_file_name, "r") as data:
        for line in data:
            line = line.strip()
            if not line:
                continue
            part = line.split(",")
            operation = part[0]
            amount = int(part[1])
            if operation == "buy":
                buy += amount
            if operation == "supply":
                supply += amount

    result = supply - buy
    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
