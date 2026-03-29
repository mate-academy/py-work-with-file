def create_report(data_file_name: str, report_file_name: str):
    buy = 0
    supply = 0

    with open(data_file_name, "r") as f, open(report_file_name, "w") as report:
        for line in f:
            line = line.split(",")
            if line[0] == "buy":
                buy += int(line[1].rstrip())
            elif line[0] == "supply":
                supply += int(line[1].rstrip())

        result = supply - buy

        report.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{result}\n"
        )
