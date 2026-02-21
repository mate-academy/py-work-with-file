def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as f:
        data_file = f.read()
    for line in data_file.splitlines():
        part = line.split(",")
        if part[0] == "supply":
            supply += int(part[1])
        if part[0] == "buy":
            buy += int(part[1])
    result = supply - buy
    with open(report_file_name, "w") as r:
        r.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
