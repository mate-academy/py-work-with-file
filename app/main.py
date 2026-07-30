def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    supply = 0
    buy = 0
    first_file = open(data_file_name, "r")
    second_file = open(report_file_name, "w")
    for line in first_file.readlines():
        line = line.strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split(",")]
        if len(parts) != 2:
            continue
        if parts[0] == "supply":
            supply += int(parts[1])
        if parts[0] == "buy":
            buy += int(parts[1])
    result = supply - buy
    second_file.write(f"supply,{supply}\n")
    second_file.write(f"buy,{buy}\n")
    second_file.write(f"result,{result}\n")
    second_file.close()
    first_file.close()
