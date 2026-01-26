def create_report(data_file_name: str, report_file_name: str) -> None:
    total = {}
    with open(data_file_name, "r", encoding="utf-8") as file1:
        for line in file1:
            line = line.strip()
            if not line:
                continue

            operation_type, amount = line.split(",")
            if operation_type not in total:
                total[operation_type] = 0

            total[operation_type] += int(amount)
    result = total.get("supply", 0) - total.get("buy", 0)

    with open(report_file_name, "w", encoding="utf-8") as file2:
        file2.write(f"supply,{total.get("supply", 0)}\n")
        file2.write(f"buy,{total.get("buy", 0)}\n")
        file2.write(f"result,{result}\n")
