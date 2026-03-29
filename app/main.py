def create_report(data_file_name: str, report_file_name: str) -> None:
    source = open(data_file_name)
    supply = 0
    buy = 0
    for line in source.readlines():
        line = line.split(",")
        if line[0] == "supply":
            supply += int(line[1])
        elif line[0] == "buy":
            buy += int(line[1])
    result = supply - buy
    source.close()
    destination = open(report_file_name, "w")
    destination.write(f"supply,{supply}\n")
    destination.write(f"buy,{buy}\n")
    destination.write(f"result,{result}\n")
    destination.close()
