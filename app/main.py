def create_report(data_file_name: str, report_file_name: str) -> None:
    start_file = open(data_file_name, "r")
    supply, buy = 0, 0
    for value in start_file.read().split():
        if value.split(",")[0] == "supply":
            supply += int(value.split(",")[1])
        if value.split(",")[0] == "buy":
            buy += int(value.split(",")[1])
    result = open(report_file_name, "w")
    result.write(
        f"supply,{supply}\n"
        f"buy,{buy}\n"
        f"result,{supply - buy}\n"
    )
