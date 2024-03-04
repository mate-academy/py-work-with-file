def create_report(data_file_name: str, report_file_name: str):
    buy = 0
    supply = 0

    with open(data_file_name, "r") as f:
        for line in f:
            if line.startswith("buy"):
                buy += int(line[4:])
            elif line.startswith("supply"):
                supply += int(line[7:])

    with open(report_file_name, "w") as f:
        f.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{supply - buy}\n"
        )
