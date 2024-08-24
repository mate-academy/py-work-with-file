def create_report(data_file_name: str, report_file_name: str) -> None:
    supply, buy = 0, 0
    data_file = open(f"{data_file_name}")

    for line in data_file:
        if line.split(",")[0] == "supply":
            supply += int(line.split(",")[1])
        elif line.split(",")[0] == "buy":
            buy += int(line.split(",")[1])

    data_file.close()

    report_file = open(f"{report_file_name}", "w")
    report_file.write(f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n")
    report_file.close()
