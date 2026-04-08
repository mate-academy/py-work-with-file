def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as f:
        lines = f.readlines()

    supply = 0
    buy = 0

    for line in lines:
        if not line:
            continue

        splited = line.strip().split(",")
        if splited[0] == "supply":
            supply += int(splited[1])
        elif splited[0] == "buy":
            buy += int(splited[1])

    result = supply - buy

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
