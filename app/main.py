def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as source:
        lines = [line.split(",") for line in source.readlines()]
        print(lines)
    supply = 0
    buy = 0
    for line in lines:
        if line[0] == "supply":
            supply += int(line[1])
        if line[0] == "buy":
            buy += int(line[1])
    with open(report_file_name, "w") as output:
        output.write(f"supply,{supply}\n")
        output.write(f"buy,{buy}\n")
        output.write(f"result,{supply - buy}\n")
