def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            parts = line.split(",")
            if parts[0] == "supply":
                supply += int(parts[1])
            if parts[0] == "buy":
                buy += int(parts[1])
    result = supply - buy
    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\n")
        f.write(f"buy,{buy}\n")
        f.write(f"result,{result}\n")
