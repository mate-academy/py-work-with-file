def create_report(data_file_name: str, report_file_name: str) -> int:
    supply = 0
    buy = 0
    with open(data_file_name, "r", encoding="utf-8") as f:
        for line in f:
            operation = line.strip().split(",")[0]
            amount = line.strip().split(",")[1]
            if amount.isdigit():
                if "buy" == operation:
                    buy += int(amount)
                if "supply" == operation:
                    supply += int(amount)
    result = supply - buy
    with open(report_file_name, "w", encoding="utf-8") as f:
        f.write(f"supply,{supply}\n")
        f.write(f"buy,{buy}\n")
        f.write(f"result,{result}\n")
    return result
