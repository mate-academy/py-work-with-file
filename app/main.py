def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as f:
        lines = f.read().splitlines()
        supply = 0
        buy = 0
        for line in lines:
            if not line:
                continue
            parts = line.split(",")
            operation = parts[0]
            amount = int(parts[1])
            if operation == "buy":
                buy += int(amount)
            if operation == "supply":
                supply += int(amount)
        result = supply - buy
        file_rep = open(report_file_name, "w")
        file_rep.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
        file_rep.close()
