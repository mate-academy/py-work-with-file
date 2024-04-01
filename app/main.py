def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data:
        content = data.readlines()
    supply, buy = 0, 0
    for line in content:
        if "supply" in line:
            supply += int(line.split(",")[1])
        elif "buy" in line:
            buy += int(line.split(",")[1])
    result = supply - buy

    with open(report_file_name, "w") as data:
        data.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
