def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        lines = [line.strip().split(",")
                 for line in file.readlines() if line.strip()]
    supply = 0
    buy = 0
    for line in lines:
        if line[0] == "supply":
            supply += int(line[1])
        elif line[0] == "buy":
            buy += int(line[1])
    result = supply - buy
    with open(report_file_name, "w") as file_rep:
        file_rep.write(f"supply,{supply}\n")
        file_rep.write(f"buy,{buy}\n")
        file_rep.write(f"result,{result}\n")
