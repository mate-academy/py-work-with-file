def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(f"../{data_file_name}") as f:
        buy_total = 0
        supply_total = 0
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) < 2:
                continue
            operation = parts[0]
            amount = parts[1]
            if operation == "buy":
                buy_total += int(amount)
            elif operation == "supply":
                supply_total += int(amount)
        with open(report_file_name, "w") as e:
            e.write(f"supply,{supply_total}\nbuy,{buy_total}\n"
                    f"result,{supply_total - buy_total}\n")
