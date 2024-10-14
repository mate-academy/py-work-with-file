def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    data = open(data_file_name)
    report = open(report_file_name, "w")

    for line in data.readlines():
        value = int(line.split(",")[1])
        if "supply" in line:
            supply += value
        if "buy" in line:
            buy += value

    report.write(
        f"supply,{supply}\n"
        f"buy,{buy}\n"
        f"result,{supply - buy}\n"
    )

    data.close()
    report.close()
