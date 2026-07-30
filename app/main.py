def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    input_file = open(data_file_name)
    supply, buy = 0, 0

    for line in input_file:
        info = line.strip().split(",")

        if info[0] == "supply":
            supply += int(info[-1])

        elif info[0] == "buy":
            buy += int(info[-1])
    input_file.close()

    report_file = open(report_file_name, "w")
    report_file.write(
        f"supply,{supply}\n"
        f"buy,{buy}\n"
        f"result,{supply - buy}\n"
    )
    report_file.close()
