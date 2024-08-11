def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        for line in file:

            line = line.strip().split(",")
            if line[0] == "supply":
                supply += int(line[1])
            elif line[0] == "buy":
                buy += int(line[1])

    result = supply - buy

    with open(report_file_name, "w") as report:
        report.write(f"supply, {supply}\n")
        report.write(f"buy, {buy}\n")
        report.write(f"result, {result}\n")
