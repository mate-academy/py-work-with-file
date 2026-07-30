def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:

    reaf_file = open(data_file_name)
    supply = 0
    buy = 0
    for line in reaf_file:

        parts = line.strip().split(",")

        if parts[0] == "supply":
            supply += int(parts[1])

        if parts[0] == "buy":
            buy += int(parts[1])

    result = supply - buy

    result_file = open(report_file_name, "w")

    result_file.write(f"supply,{supply}\n")
    result_file.write(f"buy,{buy}\n")
    result_file.write(f"result,{result}\n")

    reaf_file.close()
    result_file.close()
