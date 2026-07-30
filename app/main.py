def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith("supply"):
            supply += int(line.split(",")[1])
        elif line.startswith("buy"):
            buy += int(line.split(",")[1])
    result = supply - buy

    with open(report_file_name, "a") as f:
        f.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
