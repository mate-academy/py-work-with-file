def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file_in:
        for line in file_in:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) == 2:
                operation, amount = parts[0], int(parts[1])
                if operation == "supply":
                    supply += amount
                elif operation == "buy":
                    buy += amount
        result = supply - buy
    with open(report_file_name, "w") as file_out:
        file_out.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
