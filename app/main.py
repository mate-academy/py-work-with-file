def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as source:
        while True:
            line = source.readline().split(",")
            if line == [""]:
                break
            if line[0] == "supply":
                supply += int(line[1][:-1])
            if line[0] == "buy":
                buy += int(line[1][:-1])

    with open(report_file_name, "w") as report:
        report.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{supply - buy}\n"
        )
