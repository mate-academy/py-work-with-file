def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            key, value = line.split(",", 1)
            value = int(value)
            if key == "supply":
                supply += value
            elif key == "buy":
                buy += value
    result = supply - buy
    with open(report_file_name, "w") as out:
        out.write(f"supply,{supply}\n")
        out.write(f"buy,{buy}\n")
        out.write(f"result,{result}\n")
