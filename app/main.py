def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        supply = 0
        buy = 0
        for line in file:
            if not line.strip():
                continue
            print(line.strip())
            parts = line.strip().split(",")
            operation = parts[0]
            amount = int(parts[1])
            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount
        result = supply - buy
        with open(report_file_name, "w") as files:
            files.write(f"supply,{supply}\n")
            files.write(f"buy,{buy}\n")
            files.write(f"result,{result}\n")
