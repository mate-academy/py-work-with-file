def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as f:
        content = f.read()

    supply = buy = 0
    lines = content.splitlines()

    for line in lines:
        key, value = line.split(",")
        if key == "supply":
            supply += int(value)
        if key == "buy":
            buy += int(value)

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
