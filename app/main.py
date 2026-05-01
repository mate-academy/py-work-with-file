def create_report(data_file_name: str, report_file_name: str) -> str:
    with open(data_file_name, "r") as file:
        supply = 0
        buy = 0
        for line in file:
            if not line.strip():
                continue
            parts = line.strip().split(",")
            operation = parts[0]
            amount = int(parts[1])
            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount
        result = supply - buy
    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply}\n")
        file.write(f"buy,{buy}\n")
        file.write(f"result,{result}\n")
