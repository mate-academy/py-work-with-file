def create_report(
    data_file_name: str,
    report_file_name: str
) -> None:
    old_file = open(data_file_name, "r")
    new_file = open(report_file_name, "a")

    supply = 0
    buy = 0

    for item in old_file:
        if "supply" in item:
            supply += int(item.split(",")[1])
        if "buy" in item:
            buy += int(item.split(",")[1])

    new_file.write(
        "supply," + str(supply) + "\n"
        + "buy," + str(buy) + "\n"
        + "result," + str(supply - buy) + "\n"
    )

    old_file.close()
    new_file.close()
