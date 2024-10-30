def create_report(data_file_name: str, report_file_name: str) -> None:

    w_file = open(data_file_name)
    list_text = w_file.readlines()

    buy = 0
    supply = 0

    for line in list_text:
        line = line[:len(line) - 1]

        if line[:6] == "supply":
            supply += int(line[7:])
        if line[:3] == "buy":
            buy += int(line[4:])

    result_file = open(report_file_name, "w")
    result_file.write(
        "supply," + str(supply)
        + "\nbuy," + str(buy)
        + "\nresult," + str(supply - buy) + "\n"
    )

    result_file.close()
    w_file.close()

    return
