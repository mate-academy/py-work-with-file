
def create_report(data_file_name: str, report_file_name: str) -> None:
    buy = 0
    supply = 0
    with open(data_file_name, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            op = parts[0]
            amount = int(parts[1])
            if op == "supply":
                supply += amount
            elif op == "buy":
                buy += amount
    result = supply - buy
    with open(report_file_name, "w", encoding="utf-8", newline="") as f:
        f.write(f"supply,{supply}\n")
        f.write(f"buy,{buy}\n")
        f.write(f"result,{result}\n")
