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
    source.close()

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\n"
                     f"buy,{buy}\n"
                     f"result,{supply - buy}\n")
    report.close()
